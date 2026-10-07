import json,glob,os,collections
d=collections.defaultdict(lambda: collections.Counter())
for f in glob.glob('/Users/dev/.claude/projects/**/*.jsonl',recursive=True):
    sub='subagents' in f or '/agent-' in f
    proj=f.split('/projects/')[1].split('/')[0]
    try:
        for line in open(f,errors='ignore'):
            if '"assistant"' not in line: continue
            try: o=json.loads(line)
            except: continue
            if o.get('type')!='assistant': continue
            m=o.get('message',{}).get('model'); ts=o.get('timestamp','')[:10]
            if not m or m=='<synthetic>': continue
            d[(m,'sub' if sub else 'main')][ts]+=1
    except Exception as e: pass
for k in sorted(d):
    days=sorted(d[k]); 
    print(k, days[0], days[-1], sum(d[k].values()), 'days:',len(days))
    print('   ', ' '.join(f"{x[5:]}:{d[k][x]}" for x in days))
