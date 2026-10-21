# BOCIPT member chatbot — functional specification

**Status:** Draft for CSI  
**Date:** 21 October 2026  
**Audience:** CSI, to design and build against. BOCIPT Pension Services and Business Technology, to confirm.  
**What this document is:** The behaviour, the data the bot may use, and the constraints that are not optional.  
**What this document is not:** The technical design. CSI writes that, and it is checked against this spec.  
**User journeys:** Detailed journeys will be attached. They have to follow the rules in this document. They do not add scope by themselves.

Working titles, as used for the regulator pack:

| Level | Title | Who | Status |
| --- | --- | --- | --- |
| 1 | AI Digital Ambassador | Anyone, before login | Baseline |
| 2 | Smart AI Member Engagement | A logged-in member | Baseline |
| 3 | Smart AI Member Awareness | A logged-in member | Sandbox test, not the baseline |

---

## 1. Purpose and boundary

BOCIPT wants a chatbot on its member website and mobile app. It answers questions about MPF and about the member’s own account, using material BOCIPT has approved and figures BOCIPT already shows.

Since 5 June 2025 the line is:

> The member can view with BOCIPT. The member acts on eMPF.

Viewing means balance, fund split, contribution history, and statements. Acting means a switch, a withdrawal, a transfer, or a contribution. Those instructions are submitted to eMPF. The bot names the form and gives the public pointer. It does not walk the member through eMPF screens, and it does not submit anything.

**In scope**

- Prospects and members of BOCIPT’s two MPF schemes, on the website and the app.
- Read-only answers after login.
- An internal portal for Pension Services and IT, specified in section 3.6. Members never see it.

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
| Member chatbot | Prospect and member | One chatbot service, shown in two places: the member website and the mobile app. Both use the same backend. |
| Internal portal | Pension Services and IT | A separate staff web application. It is how the service is run. It is not a third chat channel, and members do not open it. |

---

## 2. Users and channels

| User | Where | Login | What they can get |
| --- | --- | --- | --- |
| Prospect, or anyone not logged in | Website or app | No | Public facts only. Level 1. |
| MPF member | Website or app | Yes, the existing member login | Level 1, plus their own account (Level 2). Level 3 only inside the sandbox test. |
| Pension Services admin | Internal portal | Internal | Loads and checks the library. Does not change the model or the refusal rules. |
| IT admin | Internal portal | Internal | Accounts, logs, troubleshooting. Does not change what members are told. |

A typed account number, HKID, or name is not a login. Without the existing member session, the bot has no account data.

The member site is in English and Traditional Chinese. The bot answers in the language the member is using, from material held in that language. Simplified Chinese is not confirmed.

---

## 3. Functional requirements

### 3.1 The three levels

**Level 1 — AI Digital Ambassador.** Before login. Statutory MPF facts and BOCIPT’s own published scheme and fund facts. No member record is read.

**Level 2 — Smart AI Member Engagement.** After login. Read-only retrieval of that member’s account, plus guidance to pages that already exist on the member site. A chart, where shown, is drawn from those retrieved figures. The bot does not calculate a new projection.

**Level 3 — Smart AI Member Awareness.** Sandbox only. Two behaviours, both factual:

- **Financial wellness.** Approved concepts: how a saving habit works, what a tax-deductible contribution is, what a statement is for. The aim is understanding. It is not a product offer and not a judgement on this member’s position.
- **Timely update.** A notice BOCIPT has already published. Examples discussed: three new funds on a scheme, the tax-deductible contribution window in that season, the annual benefit statement being available. The notice can be the first thing shown when the chat opens. It can also be attached after an answer. It is not chosen from the member’s holdings, age, or risk.

Levels 1 and 2 must work with Level 3 switched off.

### 3.2 Speaking rules

Every reply falls in one cell. The cell is decided by two questions: is this a fact or a recommendation, and did the member ask or did we raise it?

|  | Member asks | We raise it |
| --- | --- | --- |
| **Fact** | **Fact.** Answer from approved material or from that member’s record. | **Addendum.** A published timely update. Sandbox. |
| **Recommendation** | **Refusal.** The bot declines and states the limit. | **Out.** Not built. |

**Value-added service sits inside Fact.** The member asks how a task is done: which form, which channel owns it, where a payment is received, which page on the member site shows a figure. The bot names the form, the channel, and the public pointer, from approved material. It does not teach the clicks on eMPF.

**Financial wellness sits between Fact and Addendum.** If the member asks how a concept works, the reply is a Fact from approved material. If the bot raises a concept without a question, that raising is an Addendum: sourced, not personal, sandbox only.

**Referral is not a fifth mode.** If the member themselves raises a bank or partner topic, the bot finishes the MPF answer first. Any pointer beyond that is only what an approved document already says. The bot does not ask whether the member banks with a group company, does not open with an offer, and does not take an application.

### 3.3 What the bot never does

- Recommend a fund, a scheme, a switch, or a contribution amount.
- Say that something suits this member’s age, risk, or goal.
- Forecast a balance, a return, or whether the member is “on track”.
- Compare BOCIPT with another trustee, or this member with other members.
- Rank funds against each other as a suggestion.
- Invent a fee, a performance figure, a date, or a rule.
- Describe eMPF screen by screen.
- Use the member’s record to decide which notice to show.
- Answer from the open web, or from a document that is not in the approved library.

If the library and the account data do not contain the answer, the bot says it does not know. It does not fill the gap.

### 3.4 Scenarios

Journeys for these scenarios will be attached. The behaviour below is the requirement.

#### Level 1

**S1 — Understanding MPF.**  
Public rules a person needs before they have an account: what MPF is, contribution types, tax-deductible voluntary contributions as a published rule, and which door owns which task.  
Does: answer from approved public material and cite it.  
Refuses: which fund to pick, whether this person should join, whether they should pay more.

**S2 — Our schemes and funds.**  
BOCIPT’s own schemes, funds, fees, fact sheets, and the asset manager information BOCIPT already publishes. Standing facts, not only news.  
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

**S6 — Financial wellness.**  
Concepts from approved material: saving habits, what the tax-deductible contribution is for, how to read a statement.  
Does: explain the concept. Cites the source.  
Refuses: “you should top up”, “this fund fits you”, or a gap between the member and a retirement target.

**S7 — Timely update.**  
A notice already published by BOCIPT.  
Does: show it when the chat opens, or attach it to an answer, with its source.  
Refuses: to pick the notice from this member’s funds, age, or behaviour, and to turn the notice into an instruction.

### 3.5 Conversation behaviour

- Before login, account questions are refused. The bot tells the member to sign in with the existing member login. It does not collect identity in the chat.
- After logout, account answers stop.
- A factual answer cites the document or the account source it came from.
- A timely update cites the notice.
- The model does not invent the numbers in a chart. The chart is rendered from the fields retrieved for that request.
- The bot answers, or it says it cannot. It does not hand the conversation to a person.
- Language follows the member’s channel language, limited to languages the library actually holds.

How long a conversation is kept, and whether it continues across visits, is open. See section 6.

### 3.6 Internal portal

Staff do not run the chatbot from the member website or the app. They use a separate web portal on the same platform. Members never open it.

Pension Services is accountable for what the bot says. They are not technical, and they do this between calls, so a content change must not need an IT ticket. IT runs access and supports the platform, and must not be able to change what members are told.

| Capability | Pension Services admin | IT admin |
| --- | --- | --- |
| Library — add, edit, enable, disable, delete | Full | Read only |
| Activity log | View | View and export |
| Playground and golden test set | Full | View only |
| Conversation review | Full | View only |
| Provision or revoke a Pension Services admin | No | Yes |
| System prompt, model temperature, agent building blocks | Locked | Locked |
| Refusal rules | Set at build. Not editable. | Set at build. Not editable. |

Every restriction is enforced on the server. Hiding a control in the screen is not enough. It must hold when the interface is called directly with the wrong role.

The library, the activity log, access control, the playground, and conversation review are required. The playground is not optional. It is removed only if CSI pushes back on price and BOCIPT accepts that in writing (O11).

#### Library — must have

| ID | Requirement |
| --- | --- |
| P1 | Upload a folder of approved documents in one action. Report which files succeeded and which failed. Retry only the failures. One bad file does not fail the whole batch. |
| P2 | Add one question and answer, and publish it. Warn if a near-duplicate is already in the library. |
| P3 | Edit an entry and save. The chatbot uses the new text immediately. If a colleague changed the same entry while it was open, say so. Do not silently overwrite. |
| P4 | Disable an entry immediately. It stops being used at once, not at a later rebuild. The content is kept. |
| P5 | Restore a disabled entry. Warn if the source document has been replaced since it was disabled. |
| P6 | Delete permanently only after confirmation, and state that it cannot be undone. If the entry is live and in use, require a second confirmation. |
| P7 | Every entry has exactly one category. The portal supports at least: scheme information, forms, fund facts, complaints, and member guidance. |
| P8 | Search and filter by category, status, language, and keyword. Search looks inside the content, not only the title. |
| P9 | One status screen: what is live, what is disabled, what is waiting for review, and what is missing a language version. |
| P10 | When a new document replaces an old one, flag every entry sourced from the old document for review. List those flags together, and show them on the status screen. |
| P11 | Load content now and set the date it goes live. Cancel or move that date before it takes effect. |
| P12 | For each entry, show which in-scope language versions exist and which are missing. Publishing in one language only is an explicit choice, not the default. |

An edit to a live entry takes effect immediately (P3, P4). New material can be held until a date (P11). Those are different actions.

#### Activity log and access — must have

| ID | Requirement |
| --- | --- |
| P13 | Pension Services can open an entry’s history: the named person, the time, and the text before and after. Nobody can edit or delete that history, including Pension Services. |
| P14 | IT can export the activity log for a date range. The export includes failed and rejected attempts. |
| P15 | Pension Services manages the library, the playground, and conversation review without a further approval step. They cannot change the system prompt, the model settings, or the refusal rules. |
| P16 | IT can read the library and its history. Add, edit, enable, disable, and delete are unavailable to IT on the server. |
| P17 | IT can open the playground and conversation review to troubleshoot. IT cannot change the golden test set or a saved baseline. |
| P18 | IT grants and revokes Pension Services admin by name. It takes effect immediately, including a session that is already open, and it is recorded. Pension Services cannot grant this role. |

#### Playground — required

A private test, before members can see a change. Pension Services types a question and reads the answer the bot would give. It is not a member conversation. The golden set is the fixed list of questions rerun after a change, to see what moved.

This is required. It is removed only if CSI pushes back on price and BOCIPT accepts that in writing (O11).

| ID | Requirement |
| --- | --- |
| P19 | Before publishing, type a question in a private playground and see the answer the bot would give. Those turns are not written into member conversation records. |
| P20 | Show which library item produced an answer, and which part of it. Say clearly when nothing matched. |
| P21 | Hold a golden set of questions and expected answers. The expected answer is a meaning, not an exact sentence. |
| P22 | Run the golden set and compare it with the last known-good result. Show which questions changed, not only a count. |
| P23 | After an edit, show the before and after answer for every golden-set question that the edit affected. |
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
| P29 | Create a library entry from an unanswered question. Carry the member’s wording across, link the question to the new entry, and take it off the queue once it is filled. |
| P30 | Report conversation volume, sessions, and the answer rate for any period, and export that report. |

Where conversation records exist, member identifiers in them are masked or withheld unless there is a recorded reason. That rule is mandatory. BOCIPT and Compliance set it. See section 5.3.

#### Not available in the portal

- Editing the system prompt, the model temperature, or the agent building blocks. Staff cannot version these, and there is no rollback of them.
- Editing the refusal rules. BOCIPT supplies the rules. The vendor configures them at build.
- Handing a chat to a person.

### 3.7 Library

The bot answers public questions only from the library Pension Services loads and approves in the portal. If it is not in the library, the bot does not know it.

The vendor builds the portal actions in section 3.6. Choosing the documents, writing the answers, and deciding that a document is fit to publish are Pension Services’ job, not the vendor’s.

Account answers in Level 2 come from the member record, not from this library. The library does not contain member records.

---

## 4. Data integration

The bot reads. It does not write. It does not become a second system of record.

### 4.1 Sources

| ID | Source | Direction | Used for |
| --- | --- | --- | --- |
| DI-1 | Approved library, loaded by Pension Services | Read | Level 1 answers, wellness concepts, timely updates |
| DI-2 | Existing member website and mobile app | Embed the chat; share the logged-in session | Channel and identity |
| DI-3 | The account data the member site already shows | Read only, for the logged-in member | Level 2 |
| DI-4 | Statements already held for that member | Read only, or the download the site already offers | S4 |
| DI-5 | eMPF | No system connection | A form name and a public address, taken from the library |
| DI-6 | Internal portal | Internal users only | Library and operations |

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
- Member account data is not sent to a service outside BOCIPT’s control. Where the sandbox runs, and whether any data may leave the data centre for that run, is open. Until it is agreed, account data stays in the data centre.
- Conversation records, the library, and logs stay on premise. They are not sent to a public model service, and they are not used to train a model.

### 4.4 Freshness

eMPF now administers the schemes. BOCIPT’s own pages may not update at the same moment as eMPF. The bot reports the figure it was given. Where the source provides an as-at time, the bot shows it. The bot does not adjust the figure and does not claim it matches eMPF.

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
| Peak concurrent chats | Not known | CSI sizes to a peak BOCIPT states. Until then the peak is an assumption, written down, not a silent guess. |

The design states the peak it was sized for. A later change to that peak is a change of scope.

### 5.3 Security

- Chat records, the library, and logs are held on premise.
- Data in transit is encrypted. Account data and chat records are encrypted at rest.
- The member’s session is checked on the server for every account request. Hiding a control in the screen is not sufficient.
- One member cannot retrieve another member’s account by changing an identifier in the request.
- Pension Services cannot grant the admin role. IT cannot change library content that members are told.
- IT can troubleshoot without seeing member data by default. Seeing it requires a recorded reason. The rule is set by BOCIPT and Compliance.
- Admin actions are logged: who did what, and when. Retrieval of account data into a conversation is logged.
- Text inside a document or a member’s message cannot switch off the speaking rules.
- Nothing in the prompt is sent to a cloud model API.

### 5.4 Compliance

- The bot does not give investment advice, does not assess suitability, and does not forecast performance.
- It does not recommend a scheme or a fund, including BOCIPT’s own funds.
- It does not solicit a bank product.
- Personal data is used to answer the member who owns it, and for the operation and audit of this service. It is not used to build a marketing profile.
- Because the bot does not carry out a suitability assessment, it does not create the suitability file that regulations require a person to keep when they do give advice.
- Every factual claim is traceable to the library or to the account fields retrieved for that turn.
- Pension Services and the project team hold a shared test of about 30 to 50 questions, half ordinary and half traps. It is rerun in the portal when the library changes and when a release changes answers. “Which fund should I pick?” remains a refusal. A release that fails a trap does not go live.
- The refusal rules are configured at build. Staff cannot edit them in the internal portal.

---

## 6. Assumptions, risks, and open points

CSI does not close an open point by choosing a convenient default. An assumption used for sizing or design is written into the design and confirmed by BOCIPT.

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
| A8 | Peak concurrent chats will be supplied by BOCIPT before sizing is treated as final. |
| A9 | Where a member has more than one account, the page they are on identifies which account, or the bot asks. |

### 6.2 Risks

| ID | Risk | What the spec already does about it |
| --- | --- | --- |
| R1 | The balance on BOCIPT’s side lags eMPF, and the member treats the chat as wrong. | Show the figure as given, with the as-at time when the source has one. Do not reconcile to eMPF. |
| R2 | A wrong answer on the official site is a trust and fraud issue, not only a content miss. | Answer only from the library and the member record. Cite the source. Say “I don’t know” when it is not there. |
| R3 | The library is not maintained, so the bot keeps an old rule. | Pension Services can withdraw an entry immediately. Content ownership stays with them. |
| R4 | Level 3 is stretched into advice or an unprompted product offer. | Speaking rules and the never-do list. The trap set must keep failing. |
| R5 | Sandbox compute sits outside the data centre, and member data follows it. | Account data does not leave until BOCIPT agrees the path. |
| R6 | Sizing uses 900,000 as if they were concurrent users. | Section 5.2. The design states its peak. |
| R7 | Chat records hold account data and are readable too widely. | Mask by default. Access by recorded reason. Retention still to be set. |

### 6.3 Open points

| ID | Point | Who confirms |
| --- | --- | --- |
| O1 | Response-time targets | BOCIPT, then CSI designs to them |
| O2 | Availability target | BOCIPT |
| O3 | Peak concurrent chats | BOCIPT |
| O4 | How long a chat and its history are kept | Compliance |
| O5 | How long admin and retrieval logs are kept | Compliance |
| O6 | Staff sign-in: company login or local accounts | Business Technology |
| O7 | Simplified Chinese. English and Traditional Chinese are in scope (A6). How those languages are indexed is confirmed before retrieval is designed. | Pension Services, then CSI |
| O8 | Where sandbox inference runs, and what data may reach it | Business Technology, with CSI |
| O9 | Whether the account source can supply an as-at time | Business Technology |
| O10 | A session code the member could quote to the call centre | Not in this build. Recorded so it is not added silently. |
| O11 | The playground (P19–P24) is required. It is removed only if CSI pushes back on price and BOCIPT accepts that in writing. | CSI, then BOCIPT |
| O12 | A named Pension Services owner for the library. About 100 staff may use the portal. The library needs an owner, not the whole department. | Pension Services |
