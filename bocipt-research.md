# BOCIPT research — verified

Everything here is from BOCIPT's own site and documents, MPFA publications, or named press sources. Where I could not confirm something, it says **unconfirmed**.

---

## 1. Scale — the Trustee's own numbers

From BOCIPT's own news release (April 2024, figures as at end-Dec 2023):

- Trustee, custodian and/or administrator for **over 330 funds**
- Assets under Administration **~HKD 290 billion**
- MPF AUA **over HKD 82 billion**
- **~900,000 MPF accounts**
- **Ranked 5th in MPF market share by AUA**

These are the Trustee's figures, so they are safe to use. The "top 5 MPF investment manager" line I gave you earlier belongs to the Asset Manager — do not use it.

Note the kickoff mentioned 7.4% / 6th place. That came from their own BT lead. Different metric or different year. Ask rather than assert.

---

## 2. Who they actually serve

### Confirmed schemes under BOCIPT trusteeship

**MPF** (on eMPF Platform since 5 June 2025):
- My Choice MPF
- BOC-Prudential Easy-Choice MPF (17 constituent funds + DIS = 18 choices)

**ORSO / occupational** (NOT on eMPF — BOCIPT handles the full operation):
- BOC-Prudential Provident Fund Scheme ("the Pool") — pooled ORSO for SMEs, 13 funds, BOCIPT became trustee 7 Dec 2018
- BOCHK Staff Provident Fund
- Government Employees MTS
- The Prudential HK Provident Fund / The Prudential Pension Plan
- VTC Provident Fund

Their published vision explicitly includes: *"Become customers' preferred retirement service provider in Hong Kong, encompassing third-party MPF and ORSO trustee and scheme administration services."*

**How many ORSO clients / members: unconfirmed.** No public figure. Ask Elaine.

### Your five user types — assessment

| Your type | Verdict | Note |
| --- | --- | --- |
| 1. Non-member / public | **Yes, with a boundary** | "What we offer" and selling is the **Asset Manager's** job — they are the registered MPF principal intermediary doing sales and marketing. The Trustee can answer scheme facts, fund facts, how to contact, how to complain. Do not let the bot pitch products. |
| 2. MPF employer | **Yes, but low value** | Administration moved to eMPF in June 2025. Mostly a routing answer. Probably not worth a workshop slot. |
| 3. MPF employee / member | **Yes — the main group** | ~900,000 accounts. Transactions go to eMPF. Information, complaints and guidance stay with BOCIPT. Your read is correct. |
| 4. ORSO employer | **Yes, and genuinely different** | Not on eMPF. BOCIPT owns the whole administration. |
| 5. ORSO employee | **Yes, and genuinely different** | Same. Full operation is BOCIPT's. |

### Two groups you missed

**6. Beneficiaries and ex-members with personal accounts.** TVC and SVC members exist in Easy-Choice (confirmed in the scheme documents). The 2 Oct kickoff named beneficiaries and TVC/SVC and put them out of scope. Keep them out, but name them so nobody thinks you forgot.

**7. BOCIPT's own staff.** The Pension Services team using the admin portal — updating the knowledge base, reading the analytics. They are a user type of the *system*, not of the chatbot. Worth stating, because it is the part Elaine's team actually touches daily.

### The ORSO insight

ORSO is the one segment where BOCIPT still owns the **entire** operation end to end. No eMPF boundary, no Asset Manager overlap, no routing problem.

That cuts both ways:
- **Good:** it is the cleanest place to prove a bot works, because there is no ownership conflict.
- **Bad:** low volume, and the sandbox story MPFA wants is member engagement at scale.

Do not push ORSO. Ask whether it matters to her. If her ORSO team is drowning in the same repeated questions, it may be a better first pilot than MPF. That would be her call, not yours.

---

## 3. What their portal already does today

From BOCIPT's Easy-Choice Customer Services Information and their e-Member pages. The logged-in dashboard already shows:

- Account balance
- Current investment mandate
- Gain / loss
- Contribution history — by fund, and by source of contribution type
- Member benefit statements
- e-statements
- Fund switching confirmation statements
- Fund price history and fund performance
- Key Scheme Information Documents, scheme brochure
- MPF forms

Also available: internet, mobile app, and ATM (BOCHK, Chiyu, JETCO).

Fund switching and investment changes are submitted **to eMPF** via its web portal or app, cut-off 4:00pm on a business day. BOCIPT no longer takes those instructions.

**What this means for your Layer 2.** You were right: the data is already there. The bot's job on Layer 2 is **retrieval and navigation** — letting a member ask instead of hunting through menus. That is cheap and low-risk. It is not new data, and it does not need new integration beyond what the portal already has. Say it that way and it stops sounding like a big project.

---

## 4. Your four information layers — verified

| Layer | Verdict | Evidence / caution |
| --- | --- | --- |
| **1. General scheme and fund info** — performance, fees, fund facts, manager info | **Safe. Already public.** | Published on bocpt.com and in the scheme documents. MPFA's Disclosure Code requires fee tables and on-going cost illustrations. This is the obvious Level 1. |
| **2. Portfolio info after login** — balance, YTD, distribution, per-fund gain/loss | **Safe, but it is retrieval, not new data** | All of it is already on the dashboard (see §3). Value = ask instead of navigate. Needs login and permission checks. Member data cannot leave the data centre yet. |
| **3. Market insights / fund price alerts** | **Split this — one half is fine, one half is not allowed** | *Fine:* a factual alert when a fund's **past** price crosses a threshold the member set. Their site already does fund price enquiry, so the data exists. *Not allowed:* "the HK market is rising so related funds could benefit." MPFA Guidelines VI.2 §III.43 says an intermediary should **"avoid predicting, projecting or forecasting a constituent fund's future or likely performance."** General market outlook may be referenced. Fund-level forecasting may not. Drop the second half unless Compliance signs it. |
| **4. What-if / retirement projection / risk analysis** | **Possible, but this is where it gets dangerous** | An illustrative projection is permitted **if** it states its assumptions, is not a prediction, and is not presented as a recommendation. MPFA runs exactly such a tool (Retirement Planning Calculator) with published assumptions: retire at 65, 5%+5% contributions, statutory income caps, user-entered net-of-fee return. **But** a suitability assessment is a different and much heavier thing — MPFA Guidelines VI.2 §III.28 requires assessing risk profile, matching fund risk to it, explaining why the fund suits the member, giving them a signed document, and keeping it for seven years. A bot must not do that. |

### The line MPFA itself drew

MPFA launched its own **"MPF Investment Education AI Assistant"** on 16 June 2026. Its stated boundary:

> provides **only objective and official information**. It would **not** offer any investment advice, recommend specific MPF schemes or funds, or assess the suitability of MPF investment products for individual scheme members.

That is your template. It is the regulator's own chatbot, running on the same theme, with the line already drawn in public. If BOCIPT's bot stays inside that line, it is defensible by definition.

Also relevant: **Governance Principles for MPF Trustees, Principle 10** — a trustee should communicate clearly and effectively, in plain language, free from false or misleading statements, and help members make informed decisions about retirement savings. That is a positive duty, not just a restriction. It is the argument for *doing* the information layer well.

**So the safe zone is: information yes, navigation yes, factual alerts yes, illustration with stated assumptions yes. Advice no, recommendation no, suitability no, forecasting no.**

That is exactly what PS and Compliance have to define. Do not define it for them. Put the line on the wall and ask them to mark it.

---

## 5. Competitor scan

Four MPF providers already have AI member tools. All four are **advisory / robo** tools, and all four were built with an outside fintech.

| Provider | Tool | What it does | Built with |
| --- | --- | --- | --- |
| **BCT** | **MARIO** | AI advisor. Portfolio recommendations, integrated chatbot as "personal MPF assistant", account navigation, quarterly review nudges. MPF Ratings singled it out, Sep 2025. | AQUMON |
| **Manulife** | **MPF Robo-Advisor** | Automated portfolio insights, asset-class and fund-level recommendations. Piloted to digitally-enabled members. Their survey: 71% of members find managing MPF investments difficult, 53% lack portfolio knowledge. | AutoML Capital + Syfe |
| **Sun Life** | **MPF Navigator** | 5-question risk profile, up to 5 reference portfolios, quarterly update notifications. Uses tokenisation so members need not submit name, gender, ID. | AQUMON |
| **AIA** | **MPF Smart Advisor** | Up to 50 portfolio options, ESG and regional preferences, comparison tool, simulate without executing switches, retirement gap calculator. Free on the AIA+ app. | Magnum Research / AQUMON |

**MPFA** | **MPF Investment Education AI Assistant** (16 Jun 2026) | Official investment-education information only. Explicitly no advice, no fund recommendation, no suitability assessment. Planned extension to their retirement planning app. | — |

No comparable AI member tool found from **HSBC** or **Hang Seng**.

### What this tells you

1. **Everybody else went for advice, via a fintech partner.** None of them built it in-house. That route needs a suitability framework, a licensed perimeter, and a vendor like AQUMON. It is not what BOCIPT's sandbox submission describes, and it is not achievable in six months.
2. **Nobody has built a service-and-routing chatbot.** Given the June 2025 eMPF migration split the member's journey across two organisations, that is a real gap — and it is BOCIPT's specific problem, not a generic one.
3. **MPFA's own bot already occupies the "information only" position.** BOCIPT can align with it rather than compete with it, and can even cite MPFA's boundary as the reason its bot is safe.
4. **Their BT team already looked at these.** In the 2 Oct meeting they named Manulife, AIA, BCT and the MPFA bot, and said they found the MPFA one broken. So this is not new information to them — but it may be new to Elaine, and it is the argument for choosing a different lane.

**The defensible position for BOCIPT:** authoritative information + navigation + routing to the right owner + anti-fraud verification. Not advice. This maps to two of MPFA's three sandbox focus areas — customer experience and anti-fraud — and avoids the one they cannot reach in six months.

---

## 6. The boundary, made concrete

Since 5 June 2025 a member's journey is split three ways. BOCIPT's own website says it directly: after onboarding, the eMPF Company provides scheme administration and handles service instructions — *"including making contributions, changing investment choices, checking account balance and withdrawing MPF"* — and members *"should no longer submit service instructions to BOCPT."*

| Topic | Owner | What the bot may do |
| --- | --- | --- |
| Contributions, withdrawals, transfers, consolidation, balance, forms, switching | **eMPF Platform** (183 2622) | Name the owner, link there. Do not process. Do not display. |
| Trustee enquiries, complaints, scheme and fund facts, e-statements, occupational schemes | **BOCIPT** | Answer from approved documents. |
| Which fund to choose, investment performance commentary, selling | **BOCI-Prudential Asset Management** | Route. Do not recommend. |
| Fake site / scam verification | **BOCIPT** | State that bocpt.com is the only official site, give the hotlines. Do not assess a specific link. |

This table is the single most useful thing you can put on the wall on Monday. Every candidate card gets stamped with a row from it.

---

## 7. What to validate with Elaine

These are the open questions your model raises. Ask, do not assume.

**On the five user types**
1. "Who does this bot serve — MPF members only, or also ORSO?"
2. "How much of your team's time goes to ORSO employers and members?" → decides whether ORSO is worth a slot or is a distraction.
3. "Do employers ever call you directly, or does everything go to eMPF now?"
4. "Do you want the bot talking to people who are not members yet?" → if yes, that is an Asset Manager conversation, not a Trustee one. Flag it.

**On the four information layers**
5. "Which of these does your team answer most often?" (put the four layers in front of her, in plain words, not as slides)
6. "Is the dashboard information enough, or do members ask for things that are not on it?"
7. "Would your team use an alert on a past fund price, or is that noise?"
8. "On projections — where is your line between an illustration and advice? Who decides?" → this is for PS and Compliance, not you. Get the name of who decides.

**On the boundary**
9. "How many of your calls are people who should have called 183 2622?" → if large, routing is your first use case.
10. "When a member asks you about a fund switch, what does your team do today?"
11. "Do members ever confuse BOCIPT with the Asset Manager, or with a fake site?" → the anti-fraud angle.

**On the competition**
12. "Have you seen BCT's MARIO, or what Manulife and AIA have done? What did you think?" → their BT team already looked. Elaine may not have. Her reaction tells you how ambitious she wants to be.

**Still unconfirmed and worth asking**
13. ORSO client and member counts — nothing public.
14. Whether the ~900,000 accounts and 5th-place ranking are still current (those were end-2023 figures).

---

## 8. The strategic conclusion to carry in

You are not helping them build a robo-advisor. Four competitors already did that, with fintech partners, and it needs a suitability framework they do not have and cannot get in six months.

You are helping them solve a problem that is **uniquely theirs**: since June 2025 their members' journey runs through two organisations, and members do not know which one to ask. BOCIPT still gets the calls.

That gives you a first use case that is cheap, low-risk, measurable, and regulator-friendly: **answer what is theirs, route what is not, and never advise.** It sits inside the boundary MPFA drew for its own AI Assistant, it hits two of MPFA's three sandbox focus areas, and it does not require member data to leave the data centre.

Everything more ambitious — projections, alerts, Level 3 — sits above that line and needs PS and Compliance to mark where the advice boundary falls. Get them to draw it. Do not draw it for them.
