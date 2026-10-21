# BOCPT chatbot — functional specification

**Status:** Draft for CSI  
**Date:** 21 October 2026  
**Audience:** CSI, to design and build against. BOCPT Pension Services and Business Technology, to confirm.  
**What this document is:** The behaviour, the data the bot may use, and the constraints that are not optional.  
**What this document is not:** The technical design. CSI writes that, and it is checked against this spec.  
**User journeys:** Detailed journeys will be attached. They have to follow the rules in this document. They do not add scope by themselves.

Working titles, as used for the regulator pack:

| Level | Title | Who | Status |
| --- | --- | --- | --- |
| 1 | AI Digital Ambassador | General public and members | Baseline |
| 2 | Smart AI Member Engagement | A logged-in member | Baseline |
| 3 | Smart AI Member Awareness | General public and members | Sandbox test, not the baseline |

---

## 1. Purpose and boundary

BOCPT wants a chatbot on its website and mobile app. The general public and members can use it. It answers from material BOCPT has approved. A logged-in member can also be shown figures BOCPT already displays for that account.

Since 5 June 2025, BOCPT’s MPF schemes are administered on eMPF. The member looks up the account on BOCPT: the balance, the fund split, the contribution history, and the statements. The member submits a switch, a withdrawal, a transfer, or a contribution on eMPF.

The bot follows that split. It reads the figures BOCPT already shows. For a change, it names the form and gives the public eMPF address. It does not walk the member through eMPF screens, and it does not submit the instruction.

**In scope**

- Prospects and members of BOCPT’s two MPF schemes, on the website and the app.
- Read-only answers after login.
- An internal portal for Pension Services and IT, specified in section 3.7. Members never see it.

**Out of scope**

- Employers.
- ORSO.
- A second chatbot for internal RFP work.
- Taking an instruction, or writing back to any member record.
- An integration that performs a transaction on eMPF.
- Investment advice, fund suitability, a forecast, a retirement-gap number, or a ranking against other trustees or other members.
- An unprompted bank or partner product offer.
- Live transfer of the chat into the call centre. That module was not bought.

Two applications, on one on-premise platform.

| Application | Who uses it | What it is |
| --- | --- | --- |
| Chatbot | General public and members | One chatbot service, shown on the website and the mobile app. Both use the same backend. |
| Internal portal | Pension Services and IT | A separate staff web application. It is how the service is run. It is not a third chat channel, and members do not open it. |

---

## 2. Users and channels

| User | Where | Login | What they can get |
| --- | --- | --- | --- |
| General public, not logged in | Website or app | No | Level 1 and Level 3. No account data. |
| MPF member | Website or app | Yes, the existing member login | Level 1 and Level 3, plus their own account (Level 2). |
| Pension Services admin | Internal portal | Internal | Loads and checks the library. Does not change the model or the refusal rules. |
| IT admin | Internal portal | Internal | Accounts, logs, troubleshooting. Does not change what members are told. |

Without the existing member session, the bot has no account data.

The site is in English and Traditional Chinese. The bot answers in the language the person is using, from material held in that language. Simplified Chinese is not confirmed. Personal data typed into the chat is handled in section 3.3.

---

## 3. Functional requirements

### 3.1 The three levels

**Level 1 — AI Digital Ambassador.** For the general public and for members. Approved public material. No member record is read.

**Level 2 — Smart AI Member Engagement.** For a logged-in member only. Read-only retrieval of that member’s account, plus guidance to pages that already exist on the member site. A chart, where shown, is drawn from those retrieved figures. The bot does not calculate a new projection.

**Level 3 — Smart AI Member Awareness.** For the general public and for members. Sandbox. The material is in the same approved library, tagged Level 3. A Timely Update is a published notice. It can be the first thing shown when the chat opens, or attached after an answer. The member’s account is not used to choose it.

Levels 1 and 2 work with Level 3 switched off.

A library document carries metadata, including its level, so retrieval can tell what a person who is not logged in may be shown. Level 2 is the member session. It is not a document tag.

### 3.2 Speaking rules

Every reply falls in one cell. The cell is decided by two questions: is this a fact or a recommendation, and did the member ask or did we raise it?

|  | The person asks | We raise it |
| --- | --- | --- |
| **Fact** | **Fact.** Answer from approved material, or from that member’s record when they are logged in. | **Timely Update.** A published notice from the library. Sandbox. |
| **Recommendation** | **Refusal.** The bot declines. | **Out.** Not built. |

A recommendation or advice is a refusal. The guardrail is in section 3.3. There is no fifth way of speaking.

### 3.3 Guardrails

Two guardrails apply to every channel and to the portal.

**Input.** The chatbot detects personal data in what a person types, including an identity-card number. That text is treated as sensitive. It is masked when a staff user views the conversation.

**Output.** The chatbot does not recommend and does not give advice. This includes a fund, a scheme, a switch, a contribution amount, a forecast, and a comparison. The rule is configured at build. Staff cannot turn it off in the portal.

### 3.4 What the bot never does

- Recommend a fund, a scheme, a switch, or a contribution amount.
- Say that something suits this member’s age, risk, or goal.
- Forecast a balance, a return, or whether the member is “on track”.
- Compare BOCPT with another trustee, or this member with other members.
- Rank funds against each other as a suggestion.
- Invent a fee, a performance figure, a date, or a rule.
- Describe eMPF screen by screen.
- Use the member’s record to decide which notice to show.
- Answer from the open web, or from a document that is not in the approved library.

If the library and the account data do not contain the answer, the bot says it does not know. It does not fill the gap.

### 3.5 Scenarios

Journeys for these scenarios will be attached. The behaviour below is the requirement.

#### Level 1

**S1 — Understanding MPF.**  
Public rules a person needs before they have an account: what MPF is, contribution types, tax-deductible voluntary contributions as a published rule, and which door owns which task.  
Does: answer from approved public material and cite it.  
Refuses: which fund to pick, whether this person should join, whether they should pay more.

**S2 — Our schemes and funds.**  
BOCPT’s own schemes, funds, fees, fact sheets, and the asset manager information BOCPT already publishes. Standing facts, not only news.  
Does: quote the published fact and cite the document.  
Refuses: “are your fees the lowest”, and any comparison with another trustee.

#### Level 2

**S3 — Balance, fund split, and performance.**  
The figures this member can already see after login: balance, how the account is split across funds, and the performance figures already shown for that account.  
Does: read those fields and, where a chart helps, render a fixed chart from them.  
Refuses: a new projection, a simulator, or advice to change the split.

**S4 — Contribution history and statements.**  
The contribution ledger and the statements this member can already open.  
Does: retrieve the entries and provide the statement the site already holds.  
Refuses: to produce a new statement, or to explain what the member should do next with the money.

**S5 — Finding it on the member site.**  
The member wants the page rather than the answer in the chat. The site already has screens for balances and simple analysis.  
Does: name the page and explain what that page shows.  
Refuses: to rebuild that tool inside the chat, or to walk through eMPF.

#### Level 3 — sandbox

**S6 — Level 3 library material.**  
Does: answer from a Level 3 document and cite it.  
Refuses: a recommendation or advice.

**S7 — Timely Update.**  
A notice already published by BOCPT and loaded in the library.  
Does: show it when the chat opens, or attach it to an answer, with its source.  
Refuses: to choose the notice from the member’s account, and to turn the notice into an instruction.

### 3.6 Conversation behaviour

- Before login, account questions are refused. The bot tells the member to sign in with the existing member login. It does not collect identity in the chat.
- After logout, account answers stop.
- A factual answer cites the document or the account source it came from.
- A timely update cites the notice.
- The model does not invent the numbers in a chart. The chart is rendered from the fields retrieved for that request.
- The bot answers, or it says it cannot. It does not hand the conversation to a person.
- Language follows the member’s channel language, limited to languages the library actually holds.

How long a conversation is kept, and whether it continues across visits, is open. See section 6.

### 3.7 Internal portal

Staff do not run the chatbot from the member website or the app. They use a separate web portal on the same platform. Members never open it.

Pension Services is accountable for what the bot says. They are not technical, and they do this between calls, so a content change must not need an IT ticket. IT runs access and supports the platform, and must not be able to change what members are told.

| Capability | Pension Services admin | IT admin |
| --- | --- | --- |
| Library — upload, add text, download, disable, restore, delete | Full | Read only |
| Activity log | View | View and export |
| Playground and golden test set | Full | View only |
| Conversation review | Full | View only |
| Provision or revoke a Pension Services admin | No | Yes |
| System prompt, model temperature, agent building blocks | Locked | Locked |
| Refusal rules | Set at build. Not editable. | Set at build. Not editable. |

Every restriction is enforced on the server. Hiding a control in the screen is not enough. It must hold when the interface is called directly with the wrong role.

The library, the activity log, access control, the playground, and conversation review are required.

#### Library — must have

There is no approval step. A document Pension Services uploads is available to the chatbot, unless they disable it or set a future date. There is no editing inside the portal. To change a document, staff download it, change it outside the portal, remove the old one, and upload the new one.

| ID | Requirement |
| --- | --- |
| P1 | Upload documents in a batch. Each document can be given labels at upload. Report which files succeeded and which failed. Retry only the failures. One bad file does not fail the batch. |
| P2 | Add a document by typing free text. This is a document, not a question paired with an answer. |
| P3 | Where documents overlap, the chatbot uses the newer document. |
| P4 | On upload, hash the file. If the content is a complete overlap with a document already stored, flag it and do not keep a second copy. |
| P5 | Download a document. |
| P6 | Delete a document permanently, after confirmation. State that it cannot be undone. If the document is live, require a second confirmation. |
| P7 | Disable a document. The file stays stored. The chatbot stops using it immediately. |
| P8 | Restore a disabled document. The chatbot uses it again. |
| P9 | Staff define the labels. A document can have more than one. The level tag (Level 1 or Level 3) is one of these labels. |
| P10 | Search and filter by label, status, and keyword. Search looks inside the content, not only the title. |
| P11 | One status screen: what is live, what is disabled, and what is waiting for a future date. This is not an approval queue. |
| P12 | Upload a document now and set the date the chatbot may start using it. Until that date, the chatbot cannot use it. Staff can move or cancel the date before it arrives. |
| P13 | Maintain a glossary of special names. When the chatbot answers, it uses the names in that glossary. |

Retrieval uses a multimodal embedding. The portal does not keep a separate language copy of each document.

#### Activity log and access — must have

| ID | Requirement |
| --- | --- |
| P14 | The portal shows who uploaded, downloaded, disabled, restored, or deleted a document, and when. Nobody can edit or delete that log, including Pension Services. |
| P15 | IT can export the activity log for a date range. The export includes failed and rejected attempts. |
| P16 | Pension Services manages the library, the playground, and conversation review without an approval step. They cannot change the system prompt, the model settings, or the refusal rules. |
| P17 | IT can read the library and its log, and can open the playground and conversation review. Upload, free text, download, disable, restore, and delete are unavailable to IT on the server. IT cannot change the golden test set or a saved baseline. |
| P18 | IT grants and revokes Pension Services admin by name. It takes effect immediately, including a session that is already open, and it is recorded. Pension Services cannot grant this role. |

#### Playground — required

A private test, before members can see a change. Pension Services types a question and reads the answer the bot would give. It is not a member conversation. The golden set is the fixed list of questions rerun after a change, to see what moved.

| ID | Requirement |
| --- | --- |
| P19 | Before publishing, type a question in a private playground and see the answer the bot would give. Those turns are not written into member conversation records. |
| P20 | Show which library item produced an answer, and which part of it. Say clearly when nothing matched. |
| P21 | Hold a golden set of questions and expected answers. The expected answer is a meaning, not an exact sentence. |
| P22 | Run the golden set and compare it with the last known-good result. Show which questions changed, not only a count. |
| P23 | After a library change, show the before and after answer for every golden-set question that the change affected. |
| P24 | Accept the current results as the new baseline. The approval records the Pension Services admin who accepted it. IT cannot approve a baseline. |

The release test in section 5.4 is this golden set. It is run in the portal.

#### Conversation review — required

This is not the playground. The playground is a question Pension Services types, before publish. Conversation review is what real members already asked, after the chat.

Pension Services uses it to find a complaint, see which questions come up most, see what the bot could not answer, and write the missing library entry from that question. A correct refusal, such as “which fund should I pick?”, stays in its own list. It is not treated as missing content.

| ID | Requirement |
| --- | --- |
| P25 | Find a conversation by keyword, date, or topic, and read the full exchange. |
| P26 | Export a filtered set of conversations. Record who exported what, and when. These files contain member data. |
| P27 | For a chosen period, rank the most common questions and group them by meaning, with examples under each. |
| P28 | List questions the bot could not answer, ranked. Keep refusals in a separate list. A correct refusal of advice is not missing content. Show that refusal list on its own. |
| P29 | Create a library document from an unanswered question. Carry the person’s wording across, link the question to the new document, and take it off the queue once it is filled. |
| P30 | Report conversation volume, sessions, and the answer rate for any period, and export that report. |

Where conversation records exist, personal data in them is masked when staff view them. See section 3.3. BOCPT and Compliance set when a recorded reason allows the mask to be lifted.

#### Not available in the portal

- Editing the system prompt, the model temperature, or the agent building blocks. Staff cannot version these, and there is no rollback of them.
- Editing the refusal rules. BOCPT supplies the rules. The vendor configures them at build.
- Editing a library document inside the portal. Staff download it, change it outside, and upload it again.
- Handing a chat to a person.

### 3.8 Library

The bot answers from documents Pension Services loads in the portal. If it is not in the library, the bot does not know it.

The same library holds Level 1 and Level 3. Each document is tagged with its level. Level 3 does not come from a separate feed, and it is not chosen from the member’s record. A newer document is used where documents overlap.

The vendor builds the portal actions in section 3.7. Choosing the documents and deciding what is fit to publish are Pension Services’ job, not the vendor’s.

Account answers in Level 2 come from the member record, not from this library. The library does not contain member records. A logged-in member can still be answered from a Level 1 or Level 3 document.

---

## 4. Data integration

The bot reads. It does not write. It does not become a second system of record.

### 4.1 Sources

| ID | Level | Source | Direction | What it supplies |
| --- | --- | --- | --- | --- |
| DI-1 | Level 1 | Approved library, loaded by Pension Services | Read | Public MPF rules, and BOCPT scheme, fund, and fee facts |
| DI-1 | Level 3 | Approved library, loaded by Pension Services | Read | Financial wellness concepts. How a saving habit works, what a tax-deductible contribution is, what a statement is for |
| DI-1 | Level 3 | Approved library, loaded by Pension Services | Read | Timely updates. Notices BOCPT has already published, such as new funds on a scheme, the tax-deductible contribution window in that season, and the annual benefit statement being available. Shown when the chat opens, or attached after an answer. The member’s holdings, age, and risk are not used to choose it |
| DI-2 | — | Existing member website and mobile app | Embed the chat; share the logged-in session | Channel and identity |
| DI-3 | Level 2 | The account data the member site already shows | Read only, for the logged-in member | Balance, fund split, performance, contribution history, and the current investment election where the site already shows it |
| DI-4 | Level 2 | Statements already held for that member | Read only, or the download the site already offers | Statement list and file |
| DI-5 | — | eMPF | No system connection | A form name and a public address, taken from the library |
| DI-6 | — | Internal portal | Internal users only | Library and operations |

Level 1 and Level 3 are both read from the approved library, DI-1. Level 3 has no source of its own. A logged-in member still receives a Level 3 concept or notice from that library.

DI-3 is the same business information the member can see today after login:

- balance
- fund split
- gain/loss and performance figures the site already shows for that account
- contribution history
- the current investment election, if the site already shows it
- the list of statements

Field names and the interface are CSI’s design, agreed with Business Technology. The rule is the business one: no field the member cannot already see, and no field for a member who is not the one logged in.

### 4.2 Identity

- The chat uses the member site’s existing session. There is no second password.
- A Level 2 request without a valid session returns no account data.
- The bot does not treat something typed in the chat as proof of who the member is.
- Staff access to the internal portal is a named person. Whether that is the company’s existing sign-in or a local account is open.

### 4.3 What must not cross

- No instruction is sent to eMPF or back into the member record.
- A timely update is not selected by querying the member’s holdings or profile.
- Member account data is not sent to a service outside BOCPT’s control. Where the sandbox runs, and whether any data may leave the data centre for that run, is open. Until it is agreed, account data stays in the data centre.
- Conversation records, the library, and logs stay on premise. They are not sent to a public model service, and they are not used to train a model.

### 4.4 Freshness

eMPF now administers the schemes. BOCPT’s own pages may not update at the same moment as eMPF. The bot reports the figure it was given. Where the source provides an as-at time, the bot shows it. The bot does not adjust the figure and does not claim it matches eMPF.

---

## 5. Non-functional requirements

### 5.1 Performance

Targets are not yet set. CSI shall not invent them in the design and present them as agreed.

| Case | Target |
| --- | --- |
| A Level 1 answer from the library | To be confirmed |
| A Level 2 answer that reads the member record | To be confirmed |
| A chart rendered from those figures | To be confirmed |
| Availability, relative to the member website | To be confirmed |

The measure is the time until the member has the complete answer, on the web and in the app, at the peak in section 5.2.

### 5.2 Volume

| Figure | Value | How to use it |
| --- | --- | --- |
| MPF member accounts, both schemes | About 900,000 | The size of the population. Not the number of concurrent users. Confirm the figure. |
| People who may use the internal portal | About 100 in Pension Services, few of them admins | Size the portal for named staff, not for members. |
| Peak concurrent chats | Not known | CSI sizes to a peak BOCPT states. Until then the peak is an assumption, written down, not a silent guess. |

The design states the peak it was sized for. A later change to that peak is a change of scope.

### 5.3 Security

- Chat records, the library, and logs are held on premise.
- Data in transit is encrypted. Account data and chat records are encrypted at rest.
- The member’s session is checked on the server for every account request. Hiding a control in the screen is not sufficient.
- One member cannot retrieve another member’s account by changing an identifier in the request.
- Pension Services cannot grant the admin role. IT cannot change library content that members are told.
- Personal data typed into the chat is detected and masked in the portal. See section 3.3. IT can troubleshoot without seeing it by default. Seeing it requires a recorded reason. The rule is set by BOCPT and Compliance.
- Admin actions are logged: who did what, and when. Retrieval of account data into a conversation is logged.
- Text inside a document or a member’s message cannot switch off the speaking rules.
- Nothing in the prompt is sent to a cloud model API.

### 5.4 Compliance

- The bot does not give investment advice, does not assess suitability, and does not forecast performance.
- It does not recommend a scheme or a fund, including BOCPT’s own funds.
- It does not solicit a bank product.
- Personal data is used to answer the member who owns it, and for the operation and audit of this service. It is not used to build a marketing profile.
- Because the bot does not carry out a suitability assessment, it does not create the suitability file that regulations require a person to keep when they do give advice.
- Every factual claim is traceable to the library or to the account fields retrieved for that turn.
- Pension Services and the project team hold a shared test of about 30 to 50 questions, half ordinary and half traps. It is rerun in the portal when the library changes and when a release changes answers. “Which fund should I pick?” remains a refusal. A release that fails a trap does not go live.
- The refusal rules are configured at build. Staff cannot edit them in the internal portal.

---

## 6. Assumptions, risks, and open points

CSI does not close an open point by choosing a convenient default. An assumption used for sizing or design is written into the design and confirmed by BOCPT.

### 6.1 Assumptions

| ID | Assumption |
| --- | --- |
| A1 | Pension Services owns library content. The vendor owns the mechanism. |
| A2 | The member website and app can share a logged-in session with the chat. |
| A3 | The account figures in section 4.1 are already available to the member site. |
| A4 | About 900,000 is the right order of magnitude for MPF accounts. |
| A5 | Levels 1 and 2 are the build. Level 3 is built only as the sandbox test. |
| A6 | English and Traditional Chinese are the languages in scope. |
| A7 | There is no call-centre handoff in this build. |
| A8 | Peak concurrent chats will be supplied by BOCPT before sizing is treated as final. |
| A9 | Where a member has more than one account, the page they are on identifies which account, or the bot asks. |

### 6.2 Risks

| ID | Risk | What the spec already does about it |
| --- | --- | --- |
| R1 | The balance on BOCPT’s side lags eMPF, and the member treats the chat as wrong. | Show the figure as given, with the as-at time when the source has one. Do not reconcile to eMPF. |
| R2 | A wrong answer on the official site is a trust and fraud issue, not only a content miss. | Answer only from the library and the member record. Cite the source. Say “I don’t know” when it is not there. |
| R3 | The library is not maintained, so the bot keeps an old rule. | Pension Services can withdraw an entry immediately. Content ownership stays with them. |
| R4 | Level 3 is stretched into advice or an unprompted product offer. | Speaking rules and the never-do list. The trap set must keep failing. |
| R5 | Sandbox compute sits outside the data centre, and member data follows it. | Account data does not leave until BOCPT agrees the path. |
| R6 | Sizing uses 900,000 as if they were concurrent users. | Section 5.2. The design states its peak. |
| R7 | Chat records hold account data and are readable too widely. | Mask by default. Access by recorded reason. Retention still to be set. |

### 6.3 Open points

| ID | Point | Who confirms |
| --- | --- | --- |
| O1 | Response-time targets | BOCPT, then CSI designs to them |
| O2 | Availability target | BOCPT |
| O3 | Peak concurrent chats | BOCPT |
| O4 | How long a chat and its history are kept | Compliance |
| O5 | How long admin and retrieval logs are kept | Compliance |
| O6 | Staff sign-in: company login or local accounts | Business Technology |
| O7 | Simplified Chinese. English and Traditional Chinese are in scope (A6). Retrieval uses a multimodal embedding. Separate language copies are not required. | Pension Services |
| O8 | Where sandbox inference runs, and what data may reach it | Business Technology, with CSI |
| O9 | Whether the account source can supply an as-at time | Business Technology |
| O10 | A session code the member could quote to the call centre | Not in this build. Recorded so it is not added silently. |
| O11 | A named Pension Services owner for the library. About 100 staff may use the portal. The library needs an owner, not the whole department. | Pension Services |
