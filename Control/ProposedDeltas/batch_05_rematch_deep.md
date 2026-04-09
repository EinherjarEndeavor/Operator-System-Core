# PROPOSED DELTAS: BATCH 05 (RE.MATCH DEEP INGESTION)
## Sources: ShaneJohnsRe.MatchAnswers...txt, ReMatch_Doctrine_v1.0.html
## Target Databases: lifestate.db, rematch.db, rve.db

### SECTION 1: GRANULAR LIFE-STATE (lifestate.db -> profile_facts)
*Status: 1:1 Bit-Perfect Extraction*

| Category | Fact | Value | Evidence |
| :--- | :--- | :--- | :--- |
| **health** | Biological Deviations | Spinal/Neck deviations; bad back; feet conditions. | Re.Match Answers |
| **health** | Left Hand Palsy | Nerve compression palsy; arms fall asleep abnormally. | Re.Match Answers |
| **financial** | EBT Amount | $287/mo (SNAP). | Re.Match Answers |
| **financial** | Student Status | PCC Student (Eligible for student benefits). | Re.Match Answers |
| **logistics** | Housing Status | Stable (1 month); Hillsboro Shelter Indefinite. | Re.Match Answers |
| **family** | Son | Nicolai Benjamin Grieves (13); Child Support Arrears. | Re.Match Answers |
| **family** | Relationship Boundary| Asexual preference / Platonic focus / No Erika Bixby. | Re.Match Answers |
| **recovery** | Recovery Capital | Strong discipline; IOP CODA; Mandated Sobriety. | Re.Match Answers |
| **legal** | Barrier: Eviction | $15,000 damages to previous landlord. | Re.Match Answers |
| **legal** | Barrier: Overdrafts | $2,000 to multiple banks (collections). | Re.Match Answers |

### SECTION 2: RE.MATCH SYSTEM SCHEMA (rematch.db)
*Status: Initializing the 23-Category Opportunity Engine*

**Proposed Tables:**
1. **categories:** [ID, Name, Tier, LS_CMI_Alignment, Notes] (Populated from Doctrine v1.0).
2. **opportunities:** [ID, Category_ID, Name, Eligibility_JSON, Impact_Score, Contact, Status].
3. **profiles:** [ID, Intake_JSON, Constraints_JSON, Matches_JSON].

**Seed Data (Tier 0 & 1 Priority):**
- Category 1: Legal & Supervision (Static Criminal History).
- Category 2: ID & Documentation (SSN, State ID).
- Category 3: Housing & Shelter (Sober Living/Transitional).
- Category 4: Financial (Debt Tracking/SNAP).

### SECTION 3: RE.MATCH DOSSIER ACTION LOGIC (rve.db -> tasks)
*Status: Logic-Driven Execution Steps*

| Domain | Task Title | Priority | Logic |
| :--- | :--- | :--- | :--- |
| **legal** | Request expungement eligibility audit | 10 | Unlocks 2x employment access. |
| **housing** | Automate RentWell browser tasks | 9 | Stabilizes future permanent housing. |
| **logistics** | Secure New Hotspot (PCC Return imminent) | 10 | Primary internet gateway blocker. |
| **health** | PCP Referral: Martial Arts/Yoga (FlexFund) | 10 | Multiplier for Physical Training category. |

**Instructions:**
1. Review `C:\Users\tarot\Operator\Control\ProposedDeltas\batch_05_rematch_deep.md`.
2. Edit fields to ensure 100% accuracy.
3. Type "COMMIT BATCH 05" when ready.
