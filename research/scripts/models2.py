import json,glob,collections
d=collections.defaultdict(collections.Counter)
for f in glob.glob('/Users/dev/.claude/projects/**/*.jsonl',recursive=True):
    sub='subagents' in f
    proj=f.split('/projects/')[1].split('/')[0].replace('-Users-dev-','')
    for line in open(f,errors='ignore'):
        if '"assistant"' not in line: continue
        try: o=json.loads(line)
        except: continue
        if o.get('type')!='assistant': continue
        m=o.get('message',{}).get('model')
        if not m or m=='<synthetic>': continue
        d[(proj,'sub' if sub else 'main',m.replace('claude-',''))][o.get('timestamp','')[:10]]+=1
for k in sorted(d):
    days=sorted(d[k]); print(k, days[0], days[-1], sum(d[k].values()))
