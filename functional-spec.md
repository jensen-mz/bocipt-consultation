# BOCPT chatbot — functional specification

**Status:** Draft for CSI  
**Date:** 21 October 2026  
**Revision:** Restructured so each requirement is stated once. User stories are not repeated.  
**Audience:** CSI, to design and build against. BOCPT Pension Services and Business Technology, to confirm.  
**What this document is:** The behaviour, the data the system may use, and the constraints.  
**What this document is not:** The technical design. CSI writes that, and it is checked against this spec.

---

## 1. Purpose and scope

BOCPT wants a chatbot on its website and mobile app. The general public and members can use it. It answers from material BOCPT has approved. A logged-in member can also be shown figures the member site already displays.

Since 5 June 2025, BOCPT’s MPF schemes are administered on eMPF. On BOCPT the member looks up the balance, the fund split, the contribution history, and the statements. On eMPF the member submits a switch, a withdrawal, a transfer, or a contribution.

**In scope**

- The general public and members of BOCPT’s two MPF schemes, on the website and the app.
- Read-only account answers after the existing member login.
- An internal portal for Pension Services and IT. Members do not open it.

**Out of scope**

- Employers.
- ORSO.
- A second chatbot for internal RFP work.
- Taking an instruction, or writing back to any member record.
- A connection that performs a transaction on eMPF.
- Live transfer of the chat into the call centre.
- Advice, a forecast, a suitability assessment, and an unprompted product offer. The rule is CH6.

---

## 2. Users

| User | Where | Login | What they can reach |
| --- | --- | --- | --- |
| General public, not logged in | Website or app | No | Level 1 and Level 3. No account data. |
| MPF member | Website or app | The existing member login | Level 1, Level 2, and Level 3. |
| Pension Services admin | Internal portal | A named staff account | The library, the playground, and conversation review. |
| IT admin | Internal portal | A named staff account | Accounts, logs, and read-only troubleshooting. |

The site is in English and Traditional Chinese. The chatbot answers in the language the person is using, from material held in that language. Simplified Chinese is open (O7).

---

## 3. What the system connects to

Two applications sit on one platform.

| Application | Who uses it | What it is |
| --- | --- | --- |
| Chatbot | General public and members | One service, shown on the website and the mobile app. |
| Internal portal | Pension Services and IT | The staff application that runs the service. Members do not open it. |

The chatbot reads. It does not write. It is not a second system of record.

| ID | Level | Source | Direction | What it supplies |
| --- | --- | --- | --- | --- |
| DI-1 | Level 1 | Approved library, loaded by Pension Services | Read | Public MPF rules, and BOCPT scheme, fund, and fee facts |
| DI-1 | Level 3 | Approved library, loaded by Pension Services | Read | Level 3 documents, including how a saving habit works, what a tax-deductible contribution is, and what a statement is for |
| DI-1 | Level 3 | Approved library, loaded by Pension Services | Read | Timely Updates. Notices BOCPT has already published, such as new funds on a scheme, the tax-deductible contribution window in that season, and the annual benefit statement being available |
| DI-2 | — | Existing member website and mobile app | Embed the chat and share the logged-in session | Channel and identity |
| DI-3 | Level 2 | Account data the member site already shows | Read only, for the logged-in member | Balance, fund split, performance, contribution history, and the current investment election where the site already shows it |
| DI-4 | Level 2 | Statements already held for that member | Read only | Statement list and file |
| DI-5 | — | eMPF | No system connection | A form name and a public address, taken from the library |
| DI-6 | — | Internal portal | Staff only | Library and operations |

Level 1 and Level 3 are both read from DI-1. A logged-in member still receives Level 3 from that library.

DI-3 is limited to figures the member can already see after login. Field names are CSI’s design, agreed with Business Technology.

**Identity**

- The chat uses the member site’s existing session. There is no second password.
- Staff access to the portal is a named person. Company login or a local account is open (O6).

**What must not cross**

- No instruction is sent to eMPF or written back to the member record.
- A Timely Update is not chosen from the member’s holdings or profile.
- Account data stays in the data centre until BOCPT agrees any path to sandbox compute (O8).
- Conversation records, the library, and logs are not sent to a public model service and are not used to train a model.

**Freshness**

eMPF administers the schemes. BOCPT’s figures may lag. The chatbot reports the figure it was given. Where the source supplies an as-at time, the chatbot shows it. It does not adjust the figure to match eMPF.

---

## 4. Functional requirements

### 4.1 Chatbot

| Level | Title | Who | Status |
| --- | --- | --- | --- |
| 1 | AI Digital Ambassador | General public and members | Baseline |
| 2 | Smart AI Member Engagement | A logged-in member | Baseline |
| 3 | Smart AI Member Awareness | General public and members | Sandbox |

| ID | Requirement |
| --- | --- |
| CH1 | Level 1 answers from approved public material. No member record is read. |
| CH2 | Level 2 is read-only retrieval of that member’s account, and guidance to a page that already exists on the member site. |
| CH3 | Level 3 answers from library documents tagged Level 3. Levels 1 and 2 work with Level 3 switched off. |
| CH4 | A library document carries a level tag. Level 2 is the member session. It is not a document tag. |
| CH5 | Every reply is one cell of the speaking table below. |
| CH6 | The output guardrail refuses a recommendation and advice: a fund, a scheme, a switch, a contribution amount, a claim that something suits this member, a forecast, a comparison with another trustee or another member, a ranking of funds as a suggestion, an invented figure, an eMPF screen description, and an answer from the open web. |
| CH7 | The input guardrail detects personal data in what a person types, including an identity-card number, treats it as sensitive, and masks it when staff view the conversation. |
| CH8 | One chatbot service runs on the website and the app. |
| CH9 | Account data is returned only inside the existing member session, and stops when that session ends. The chat does not collect identity. |
| CH10 | For a switch, a withdrawal, a transfer, or a contribution, the chatbot names the form and gives the public eMPF address from the library. It does not submit the instruction. |
| CH11 | A chart is rendered from the figures retrieved for that request, in a fixed layout. |
| CH12 | A Timely Update is a published notice from the library. It may be the first thing shown when the chat opens, or attached after an answer. |
| CH13 | A factual answer cites its document or account source. A Timely Update cites the notice. Names follow the glossary. |
| CH14 | Where the library and, for a logged-in member, the account data do not contain the answer, the chatbot says it does not know. |
| CH15 | The chatbot answers, or it says it cannot. It does not hand the conversation to a person. |

|  | The person asks | The chatbot raises it |
| --- | --- | --- |
| **Fact** | **Fact.** From approved material, or from that member’s record when they are logged in. | **Timely Update.** A published notice. Sandbox. |
| **Recommendation** | **Refusal.** CH6. | **Out.** Not built. |

### 4.2 Internal portal

| Capability | Pension Services admin | IT admin |
| --- | --- | --- |
| Library | Full | Read only |
| Activity log | View | View and export |
| Playground and golden test set | Full | View only |
| Conversation review | Full | View only |
| Provision or revoke a Pension Services admin | No | Yes |
| System prompt, model settings, refusal rules | Locked. See CN3. | Locked. See CN3. |

| ID | Requirement |
| --- | --- |
| PO1 | The library holds documents and free text. It does not hold a question paired with an answer. |
| PO2 | A batch upload reports each file and continues when one file fails. |
| PO3 | Pension Services defines the labels. A document can carry more than one, including Level 1 or Level 3. |
| PO4 | There is no editing in the portal and no approval step. A change is a download and a new upload. |
| PO5 | A complete content overlap is detected by hash and is not stored twice. Where documents overlap, the newer document is used. |
| PO6 | Disable keeps the file and removes it from retrieval immediately. Restore returns it. |
| PO7 | Delete is permanent, confirmed once, and confirmed again when the document is live. |
| PO8 | Search covers the content and can filter by label and status. Status shows live, disabled, and scheduled. |
| PO9 | A document can be stored now and withheld until a date. That date can be moved or cancelled. |
| PO10 | A glossary of special names is maintained. CH13 uses it. Retrieval uses a multimodal embedding. Separate language copies are not required. |
| PO11 | The log records who uploaded, downloaded, disabled, restored, or deleted a document, and when. The log cannot be changed. IT can export a date range, including failed attempts. |
| PO12 | IT grants and revokes Pension Services admin by name. The change applies immediately, including an open session. |
| PO13 | A playground run is not stored as a member conversation. It shows the document and passage used, or that nothing matched. |
| PO14 | The golden set stores an expected meaning, not an exact sentence. A run shows which questions changed against the last baseline. Only a Pension Services admin can accept a new baseline. |
| PO15 | A conversation can be found by keyword, date, or topic, and read in full. An export of conversations is logged. |
| PO16 | Questions for a period can be ranked and grouped by meaning. Questions the chatbot could not answer are listed separately from refusals. |
| PO17 | An unanswered question can be saved as a library document and linked to that question. Volume, sessions, and answer rate can be exported for a period. |
| PO18 | Personal data in a conversation is masked for staff, under CH7. |

Choosing the documents is Pension Services’ job. The vendor builds the mechanism.

---

## 5. Constraints

| ID | Constraint |
| --- | --- |
| CN1 | Conversation records, the library, and logs are held on premise. |
| CN2 | Prompts are not sent to a cloud model service. Records are not used to train a model. |
| CN3 | The system prompt, model temperature, agent building blocks, and refusal rules are set at build. Staff cannot edit them. |
| CN4 | Every access rule is enforced on the server. Hiding a control on screen is not sufficient. |
| CN5 | This specification does not choose the product or the field names. CSI’s technical design is checked against it. |

---

## 6. Quality

### 6.1 Performance

Targets are not set. CSI does not fill them in and present them as agreed. The measure is the time until the person has the complete answer, on the web and in the app, at the peak in Q1.

| ID | Case | Target |
| --- | --- | --- |
| Q1 | Peak concurrent chats the design is sized for | Open. O3. The design states the peak it used. A later change of peak is a change of scope. |
| Q2 | A Level 1 answer from the library | Open. O1. |
| Q3 | A Level 2 answer that reads the member record | Open. O1. |
| Q4 | A chart rendered from those figures | Open. O1. |
| Q5 | Availability, relative to the member website | Open. O2. |

### 6.2 Volume

| ID | Figure | Value | How to use it |
| --- | --- | --- | --- |
| Q6 | MPF member accounts, both schemes | About 900,000 | The size of the population. Confirm the figure. |
| Q7 | People who may use the portal | About 100 in Pension Services, few of them admins | Size the portal for named staff. |
| Q8 | Peak concurrent chats | Not known | Q1. Do not treat 900,000 as concurrent users. |

### 6.3 Security

| ID | Requirement |
| --- | --- |
| Q9 | Data in transit is encrypted. Account data and chat records are encrypted at rest. |
| Q10 | The member session is checked on the server for every account request. One member cannot retrieve another member’s account by changing an identifier. |
| Q11 | IT sees personal data in a conversation only for a recorded reason. BOCPT and Compliance set that reason. |
| Q12 | Retrieval of account data into a conversation is logged. |
| Q13 | Text in a document or a message cannot switch off CH5 or CH6. |
| Q14 | Personal data is used to answer the member who owns it, and to operate and audit this service. It is not used to build a marketing profile. |

### 6.4 Compliance

| ID | Requirement |
| --- | --- |
| Q15 | CH6 is the rule against advice, suitability, a forecast, and a product offer. |
| Q16 | Because the chatbot does not carry out a suitability assessment, it does not create the suitability file that applies when a person does give advice. |
| Q17 | The acceptance test in section 8 is run in the portal when the library changes and when a release changes answers. A release that fails a trap does not go live. |

---

## 7. Assumptions, risks, and open points

CSI does not close an open point by choosing a default. An assumption used for design is written into the design and confirmed by BOCPT.

### 7.1 Assumptions

| ID | Assumption |
| --- | --- |
| A1 | Pension Services owns library content. The vendor owns the mechanism. |
| A2 | The member website and app can share a logged-in session with the chat. |
| A3 | The account figures in section 3 are already available to the member site. |
| A4 | About 900,000 is the right order of magnitude for MPF accounts. |
| A5 | Levels 1 and 2 are the build. Level 3 is the sandbox test. |
| A6 | English and Traditional Chinese are the languages in scope. |
| A7 | There is no call-centre handoff in this build. |
| A8 | Peak concurrent chats will be supplied by BOCPT before sizing is treated as final. |
| A9 | Where a member has more than one account, the page they are on identifies which account, or the chatbot asks. |

### 7.2 Risks

| ID | Risk | What this spec already requires |
| --- | --- | --- |
| R1 | The balance on BOCPT’s side lags eMPF, and the member treats the chat as wrong. | Report the figure as given, with the as-at time when the source has one. |
| R2 | A wrong answer on the official site is a trust and fraud issue. | CH6, CH13, and CH14. |
| R3 | The library is not maintained, so the chatbot keeps an old rule. | PO6. Content ownership stays with Pension Services. |
| R4 | Level 3 is stretched into advice or an unprompted product offer. | CH6. The trap in section 8 keeps failing. |
| R5 | Sandbox compute sits outside the data centre, and member data follows it. | Account data stays until BOCPT agrees the path (O8). |
| R6 | Sizing uses 900,000 as if they were concurrent users. | Q1 and Q8. |
| R7 | Chat records hold account data and are readable too widely. | CH7 and Q11. Retention is still open (O4). |

### 7.3 Open points

| ID | Point | Who confirms |
| --- | --- | --- |
| O1 | Response-time targets for Q2, Q3, and Q4 | BOCPT, then CSI designs to them |
| O2 | Availability target, Q5 | BOCPT |
| O3 | Peak concurrent chats, Q1 | BOCPT |
| O4 | How long a chat and its history are kept | Compliance |
| O5 | How long admin and retrieval logs are kept | Compliance |
| O6 | Staff sign-in: company login or local accounts | Business Technology |
| O7 | Simplified Chinese. Retrieval uses a multimodal embedding. Separate language copies are not required. | Pension Services |
| O8 | Where sandbox inference runs, and what data may reach it | Business Technology, with CSI |
| O9 | Whether the account source can supply an as-at time | Business Technology |
| O10 | A session code the member could quote to the call centre | Out of this build. Listed so it is not added silently. |
| O11 | A named Pension Services owner for the library | Pension Services |

---

## 8. Acceptance

| Area | How it is accepted |
| --- | --- |
| Scope, users, and connections | Inspection against sections 1 to 3. |
| Chatbot behaviour | A shared set of about 30 to 50 questions, half ordinary and half traps, including “Which fund should I pick?”. That question remains a refusal. The set is rerun under Q17. |
| Session, chart, and Timely Update | Demonstration of CH9, CH11, and CH12. |
| Portal roles | A call with the wrong role against CN4, for the matrix in section 4.2. |
| Library handling | Inspection of PO2, PO5, PO6, and PO11. |
| Constraints | Inspection that records stay on premise and that prompts are not sent to a cloud model service. |
| Performance and volume | Not accepted as agreed numbers until O1, O2, and O3 are filled. |

---

## 9. Terms and attached stories

| Term | Meaning |
| --- | --- |
| Level 1 | Public answers from the approved library. |
| Level 2 | That member’s own account, after login. Read only. |
| Level 3 | Library material tagged Level 3, including a Timely Update. Sandbox. |
| Timely Update | A notice already published by BOCPT and loaded in the library. |
| Library | The documents Pension Services loads. The only source for Level 1 and Level 3. |
| Glossary | The list of special names the answer must use. |
| Session | The existing member login on the website or app. |
| Sandbox | The Level 3 behaviour. The chatbot still runs with it switched off. |
| eMPF | The place a member submits a switch, withdrawal, transfer, or contribution. No system connection from this chatbot. |

The user stories are attached separately. They follow this specification and do not add behaviour. They cover:

- Public MPF questions
- BOCPT scheme and fund facts
- Account balance and fund split
- Contribution history and statements
- Finding an existing member page
- Level 3 library material
- Timely Update
