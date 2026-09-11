"""Publication checks that never echo a matching secret value."""
import re
import subprocess

# Include common vendor formats and generic credential assignments. Matches are
# reported by rule name only; raw values must not enter logs or Git reports.
PATTERNS = {
    'private key': r'-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----',
    'GitHub token': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b',
    'API token': r'\b(?:sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}|[sr]k_(?:live|test)_[A-Za-z0-9]{12,}|AIza[0-9A-Za-z_-]{30,}|(?:AKIA|ASIA)[A-Z0-9]{16}|xox[baprs]-[A-Za-z0-9-]{15,}|hf_[A-Za-z0-9]{25,}|glpat-[A-Za-z0-9_-]{20,})\b',
    'JWT': r'\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b',
    'credential assignment': r'''(?i)["']?(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|secret[_-]?key|password|passwd|authorization|cookie|session[_-]?(?:id|token)|cf_api_token|cloudflare_api_token)["']?\s*[:=]\s*["'][^"'\r\n]{8,}["']''',
    'bearer credential': r'(?i)\bBearer\s+[A-Za-z0-9_.~+/-]{16,}',
    'URL credential': r'(?i)\b(?:https?|postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^/\s:@]+:[^/\s@]+@',
    'signed URL': r'(?i)[?&](?:token|access_token|api_key|signature|x-amz-signature|password)=[^\s"<>]{6,}',
    'local user path': r'(?:/(?:Users|home)/[^/\s"<>]+/|[A-Za-z]:\\Users\\[^\\\s"<>]+\\)',
}


def text_findings(text):
    return [name for name, pattern in PATTERNS.items() if re.search(pattern, text)]


def pdf_text(path):
    try:
        result = subprocess.run(['pdftotext', '-layout', str(path), '-'], check=True, capture_output=True)
    except FileNotFoundError as exc:
        raise ValueError('PDF privacy check requires Poppler pdftotext') from exc
    except subprocess.CalledProcessError as exc:
        raise ValueError('PDF text extraction failed') from exc
    return result.stdout.decode('utf-8')


def check_drawing_attribution(text, expected_pages):
    values = re.findall(r'绘制[ \t]+([^\r\n]+)', text)
    return len(values) == expected_pages and all(v.strip().startswith('Lyrai LLC') for v in values)
