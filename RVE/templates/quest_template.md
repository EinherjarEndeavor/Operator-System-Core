# quest_template.md 
# RVE Quest Entry Template 
--- 
QUEST TITLE: [Title of quest] 
DOMAIN: [school | recovery | legal_admin | health_fitness | career | coding_tech | creative | relationships | finances | housing] 
TYPE: [daily | weekly | arc | crisis | bonus] 
XP REWARD: [integer, e.g. 50] 
STATUS: active 
PRIORITY: [1=normal | 2=high | 3=critical] 
DEADLINE: [YYYY-MM-DD or blank] 
SESSION ID: [optional - link to session] 
OBJECTIVE: [One sentence: What does completing this quest accomplish?] 
SUCCESS CRITERIA: - [ ] [Criterion 1] - [ ] [Criterion 2] - [ ] [Criterion 3] 
ATTRIBUTE IMPACT: - Primary: [attribute name] +[delta] - Secondary: [attribute name] +[delta] (optional) 
NOTES: [Any additional context, blockers, or linked quests] 
COMPLETED AT: [timestamp or blank] 
--- 
# TO LOG IN SYSTEM: 
# python rve/scripts/quest_engine.py --create "TITLE" DOMAIN TYPE XP [DEADLINE] 
# python rve/scripts/quest_engine.py --complete ID
