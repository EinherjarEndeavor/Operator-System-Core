# session_log_template.md 
# RVE Session Log Template 
--- 
SESSION ID: [YYYY-MM-DD-NN] 
DATE: [YYYY-MM-DD] 
START TIME: [HH:MM] 
END TIME: [HH:MM] 
DURATION: [hours:minutes] 
DOMAIN FOCUS: [primary domain for this session] 
SECONDARY DOMAINS: [comma-separated list or blank] 
SESSION TYPE: [deep_work | admin | recovery | training | social | mixed] 
ENERGY LEVEL (start): [1-5] 
ENERGY LEVEL (end): [1-5] 
FOCUS QUALITY: [1-5] 
ACCOMPLISHED: - [Item 1] - [Item 2] - [Item 3] 
QUESTS COMPLETED THIS SESSION: - Quest ID [X]: [quest title] 
QUESTS ADVANCED (partial): - Quest ID [X]: [notes on progress] 
SCORE DELTAS LOGGED: - [attribute]: +[delta] (reason: [reason]) 
BLOCKERS ENCOUNTERED: - [blocker 1] 
NEXT SESSION PRIORITY: - [Top 1-3 actions for next session] 
NOTES: [Free text - observations, insights, mood, context] 
--- 
# TO LOG SCORES AFTER SESSION: 
# python rve/scripts/score.py --log ATTRIBUTE DELTA "session:SESSION_ID" 
# python rve/scripts/quest_engine.py --complete QUEST_ID
