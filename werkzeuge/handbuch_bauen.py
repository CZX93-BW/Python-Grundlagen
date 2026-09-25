"""Build a self-contained offline reader from the handbook's Markdown files.

This renderer covers the simple Markdown forms used here. It is not a complete
CommonMark implementation; complex custom extensions may need another renderer.
"""
from html import escape
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def inline(text, source):
    """Escape text and render inline code, links and simple emphasis."""
    tokens = []

    def hold(value):
        tokens.append(value)
        return f"\x00{len(tokens)-1}\x00"

    text = re.sub(r"`([^`]+)`", lambda m: hold('<code>' + escape(m[1]) + '</code>'), text)

    def link(match):
        label, target = match[1], match[2]
        if urlsplit(target).scheme in {"https", "http"}:
            href = target
            attrs = ' target="_blank" rel="noopener noreferrer"'
        else:
            target_path = posixpath.normpath(posixpath.join(posixpath.dirname(source), target))
            if target_path.endswith('.md'):
                href = '#' + quote(target_path, safe='')
            else:
                href = target_path
            attrs = ''
        return hold(f'<a href="{escape(href, quote=True)}"{attrs}>{escape(label)}</a>')

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: tokens[int(m[1])], text)
    return text


def render(markdown, source):
    """Render the documented subset of Markdown into safe HTML."""
    lines = markdown.splitlines()
    output = []
    index = 0
    heading_number = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith('```'):
            language = line[3:].strip() or 'text'
            index += 1
            block = []
            while index < len(lines) and not lines[index].startswith('```'):
                block.append(lines[index])
                index += 1
            output.append('<div class="code-label">' + escape(language) + '</div><pre><code>' + escape('\n'.join(block)) + '</code></pre>')
            index += 1
            continue
        heading = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading:
            level = len(heading[1])
            heading_number += 1
            output.append(f'<h{level} id="section-{heading_number}">' + inline(heading[2], source) + f'</h{level}>')
            index += 1
            continue
        if line.startswith('|'):
            rows = []
            while index < len(lines) and lines[index].startswith('|'):
                cells = lines[index].strip().strip('|').split('|')
                if not all(re.fullmatch(r'\s*:?-+:?\s*', cell) for cell in cells):
                    rows.append([inline(cell.strip(), source) for cell in cells])
                index += 1
            output.append('<div class="table-wrap"><table>')
            for row_number, cells in enumerate(rows):
                tag = 'th' if row_number == 0 else 'td'
                output.append('<tr>' + ''.join(f'<{tag}>{cell}</{tag}>' for cell in cells) + '</tr>')
            output.append('</table></div>')
            continue
        list_match = re.match(r'^(?:- |\d+\. )(.+)$', line)
        if list_match:
            ordered = bool(re.match(r'^\d+\.', line))
            tag = 'ol' if ordered else 'ul'
            pattern = r'^\d+\. (.+)$' if ordered else r'^- (.+)$'
            output.append(f'<{tag}>')
            while index < len(lines):
                item = re.match(pattern, lines[index])
                if not item:
                    break
                item_text = item[1]
                if item_text.startswith('[ ] '):
                    output.append('<li class="check-item"><input type="checkbox" aria-label="Punkt abhaken"> ' + inline(item_text[4:], source) + '</li>')
                else:
                    output.append('<li>' + inline(item_text, source) + '</li>')
                index += 1
            output.append(f'</{tag}>')
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip() and not re.match(r'^(#|```|\||- |\d+\. )', lines[index]):
            paragraph.append(lines[index])
            index += 1
        output.append('<p>' + inline(' '.join(paragraph), source) + '</p>')
    return '\n'.join(output)


def category(path):
    if path.startswith('kapitel/'):
        return 'Kapitel'
    if path.startswith('90_uebungen/'):
        return 'Übungen'
    if path.startswith('91_loesungen/'):
        return 'Lösungen'
    if path.startswith(('80_praxis/', '85_projektvorlage/')):
        return 'Projekte'
    return 'Orientierung'


def main():
    documents = []
    for file in sorted(ROOT.rglob('*.md')):
        relative = file.relative_to(ROOT).as_posix()
        if any(part in {'.venv', '__pycache__', '99_archiv', 'build', 'dist'} for part in file.relative_to(ROOT).parts):
            continue
        markdown = file.read_text(encoding='utf-8')
        documents.append(dict(path=relative, title=markdown.splitlines()[0].lstrip('# '), category=category(relative), text=markdown, html=render(markdown, relative)))
    payload = json.dumps(documents, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    page = TEMPLATE.replace('__DOCUMENTS__', payload)
    (ROOT / 'START_HIER.html').write_text(page, encoding='utf-8')
    print(f'Offline-Handbuch mit {len(documents)} Dokumenten erstellt.')


TEMPLATE = r'''<!doctype html>
<html lang="de">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Python · Dein Nachschlagewerk</title>
<style>
:root{color-scheme:light;--bg:#f5f7fa;--paper:#fff;--ink:#182b40;--muted:#52677c;--line:#d9e3ed;--accent:#086b70;--soft:#e4f2f1}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 system-ui,-apple-system,"Segoe UI",sans-serif}a{color:#075d8c;text-underline-offset:3px}button,input,select{font:inherit}button,a,input,select{outline-offset:4px}header{padding:22px 32px;border-bottom:1px solid var(--line);background:var(--paper)}.brand{font-weight:760;font-size:23px;letter-spacing:-.5px}.brand span{color:var(--accent)}.meta{font-size:13px;color:var(--muted)}.layout{display:grid;grid-template-columns:320px minmax(0,1fr);max-width:1500px;margin:auto}aside{padding:24px 20px;position:sticky;top:0;height:100vh;overflow:auto;border-right:1px solid var(--line)}label{display:block;font-weight:650;font-size:14px}input[type=search],select{width:100%;background:white;border:1px solid #adbdce;border-radius:7px;padding:10px 12px;margin:6px 0 14px;color:var(--ink)}.solution-toggle{font-size:13px;font-weight:400;display:flex;gap:9px;align-items:center}.solution-toggle input{width:16px;height:16px}#count{font-size:12px;color:var(--muted);margin:16px 0 10px}.result{display:block;width:100%;border:0;border-radius:7px;padding:11px 12px;margin-bottom:5px;background:transparent;color:var(--ink);text-align:left;cursor:pointer;line-height:1.4}.result:hover{background:#edf1f5}.result[aria-current=true]{background:var(--soft);box-shadow:inset 3px 0 var(--accent)}.result small{display:block;color:var(--muted);font-size:11px;margin-bottom:3px;text-transform:uppercase;letter-spacing:.06em}main{min-width:0;padding:32px 48px 80px}.file-bar{display:flex;gap:16px;justify-content:space-between;align-items:baseline;font-size:12px;color:var(--muted);padding-bottom:20px;overflow-wrap:anywhere}article{max-width:900px;background:var(--paper);padding:34px 44px 52px;border:1px solid var(--line);border-radius:12px}h1{font-size:32px;line-height:1.22;letter-spacing:-.8px;margin:0 0 24px}h2{font-size:22px;margin:36px 0 12px;line-height:1.35}h3{font-size:18px;margin-top:28px}p{margin:0 0 17px}li{margin:7px 0}code{font:14px/1.6 ui-monospace,Consolas,monospace;background:#edf2f7;border-radius:4px;padding:2px 5px;overflow-wrap:anywhere}pre{margin:0 0 23px;padding:17px 20px;background:#13283a;color:#edf8ff;border-radius:0 0 8px 8px;overflow:auto;tab-size:4;line-height:1.65}pre code{background:transparent;padding:0;color:inherit;white-space:pre;overflow-wrap:normal;font-size:13px}.code-label{padding:5px 16px;font:11px/1.6 system-ui;text-transform:uppercase;letter-spacing:.08em;background:#213d51;color:#cae1ef;border-radius:8px 8px 0 0;margin-top:18px}.table-wrap{overflow:auto;margin:22px 0}table{width:100%;border-collapse:collapse;font-size:14px}td,th{border-bottom:1px solid var(--line);padding:11px 13px;text-align:left;vertical-align:top}th{background:#f0f5f8;font-weight:650}td:first-child{min-width:100px}.check-item{list-style:none}.check-item input{width:15px;height:15px;margin-right:8px}#toc{max-width:900px;margin-bottom:20px;font-size:14px}#toc summary{cursor:pointer;color:var(--accent);font-weight:650}#toc a{display:block;padding:3px 0}#empty{font-size:14px;color:var(--muted)}.skip{position:absolute;left:-10000px}.skip:focus{left:15px;top:10px;padding:10px;background:white;z-index:10}footer{font-size:12px;color:var(--muted);margin-top:24px}
@media(max-width:950px){.layout{grid-template-columns:270px minmax(0,1fr)}main{padding:24px}article{padding:28px}h1{font-size:28px}}
@media(max-width:700px){header{padding:18px 20px}.layout{display:block}aside{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);padding:20px}#results{max-height:240px;overflow:auto}main{padding:20px 12px 50px}article{padding:25px 20px}.file-bar{padding:0 8px 15px}h1{font-size:26px}pre{margin-left:-8px;margin-right:-8px}#toc{padding:0 8px}}
@media print{header,aside,.file-bar,#toc,footer{display:none}.layout{display:block}main,article{padding:0;border:0}pre{white-space:pre-wrap;background:#f0f0f0;color:#111}pre code{white-space:pre-wrap}a{color:inherit}}
</style></head>
<body><a class="skip" href="#reading">Zum Inhalt springen</a><header><div class="brand"><span>Python</span> / Dein Nachschlagewerk</div><div class="meta">30 Kapitel · 90 Beispiele · 30 Übungen · offline nutzbar</div></header>
<div class="layout"><aside aria-label="Dokumente suchen"><label for="query">Was möchtest du nachschlagen?</label><input id="query" type="search" placeholder="z. B. JSON, Liste löschen …" autocomplete="off"><label for="category">Bereich</label><select id="category"><option value="">Alle Bereiche</option><option>Orientierung</option><option>Kapitel</option><option>Übungen</option><option>Projekte</option><option>Lösungen</option></select><label class="solution-toggle"><input id="solutions" type="checkbox">Lösungen in die Suche aufnehmen</label><div id="count" role="status" aria-live="polite"></div><nav id="results" aria-label="Suchergebnisse"></nav><p id="empty" hidden>Keine Treffer. Versuche ein einzelnes Wort oder den Nachschlagindex.</p></aside>
<main id="reading"><div class="file-bar"><span id="path"></span><a id="original">Markdown-Datei öffnen</a></div><details id="toc"><summary>Abschnitte dieses Dokuments</summary><nav id="toc-links" aria-label="Abschnitte"></nav></details><article id="article" tabindex="-1"></article><footer>Suche: alle eingegebenen Wörter · Ctrl+K fokussiert das Suchfeld · Häkchen sind nur für diese Sitzung</footer></main></div>
<script id="documents" type="application/json">__DOCUMENTS__</script>
<script>
'use strict';
const documents = JSON.parse(document.getElementById('documents').textContent);
const byPath = new Map(documents.map(doc => [doc.path, doc]));
const query = document.getElementById('query');
const category = document.getElementById('category');
const solutions = document.getElementById('solutions');
const article = document.getElementById('article');
let current = 'README.md';
const normalize = value => value.toLocaleLowerCase('de').replaceAll('ß', 'ss');
function renderResults(){
  const words = normalize(query.value).trim().split(/\s+/).filter(Boolean);
  const results = documents.filter(doc => (solutions.checked || category.value === 'Lösungen' || doc.category !== 'Lösungen') && (!category.value || doc.category === category.value) && words.every(word => normalize(doc.text).includes(word)));
  results.sort((a,b) => {const score = doc => words.reduce((n, word) => n + (normalize(doc.title).includes(word) ? 10 : 0), 0) + (doc.path === 'README.md' && !words.length ? 50 : 0);return score(b) - score(a) || a.path.localeCompare(b.path);});
  const container = document.getElementById('results');
  container.replaceChildren();
  for(const doc of results){
    const button = document.createElement('button');button.type = 'button';button.className = 'result';button.setAttribute('aria-current', String(doc.path === current));
    const small = document.createElement('small');small.textContent = doc.category;button.append(small, document.createTextNode(doc.title));
    button.addEventListener('click', () => {if(current === doc.path){show(doc.path, true);}else{location.hash = encodeURIComponent(doc.path);}});container.append(button);
  }
  document.getElementById('count').textContent = `${results.length} Dokumente gefunden`;
  document.getElementById('empty').hidden = results.length > 0;
}
function show(path, focus=false){
  const doc = byPath.get(path) || byPath.get('README.md');current = doc.path;
  article.innerHTML = doc.html;
  document.getElementById('path').textContent = doc.path;
  const original = document.getElementById('original');original.href = doc.path;
  document.title = `${doc.title} · Python`;
  const toc = document.getElementById('toc-links');toc.replaceChildren();
  for(const heading of article.querySelectorAll('h2')){const link = document.createElement('a');link.href = '#' + heading.id;link.textContent = heading.textContent;link.addEventListener('click', event => {event.preventDefault();heading.scrollIntoView({block:'start'});});toc.append(link);}
  document.getElementById('toc').open = false;
  renderResults();
  if(focus){document.getElementById('reading').scrollIntoView({block:'start'});article.focus({preventScroll:true});}
}
function route(focus){let path='README.md';try{const candidate=decodeURIComponent(location.hash.slice(1));if(byPath.has(candidate))path=candidate;}catch{}show(path,focus);}
query.addEventListener('input', renderResults);category.addEventListener('change', renderResults);solutions.addEventListener('change', renderResults);
window.addEventListener('hashchange',()=>route(true));
document.addEventListener('keydown',event=>{if((event.ctrlKey||event.metaKey)&&event.key.toLowerCase()==='k'){event.preventDefault();query.focus();query.select();}});
route(false);
</script></body></html>'''

if __name__ == '__main__':
    main()
