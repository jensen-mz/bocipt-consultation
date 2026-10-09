# User groups, information levels, and user stories

## 1. User groups — confirmed, three

| # | Group | Login | Note |
| --- | --- | --- | --- |
| **U1** | Prospect — public, non-member | No | Can only get facts. Anything that sells belongs to the **Asset Manager**, who is the registered MPF principal intermediary |
| **U2** | Member — employee and self-employed | Yes | ~900,000 accounts. MPF only |
| **U3** | Internal — PS team | Internal | Operates the knowledge base, reviews chats, takes escalations, reads analytics |

**ORSO is out.** Confirmed. Both MPF schemes went onto eMPF on 5 June 2025; ORSO stays fully trustee-run, so it would have been the cleanest pilot — but it is out of this sandbox.

**U3 is not a "level".** It is the operating layer underneath U1 and U2. Somebody has to load the FAQ, review unanswered questions, take escalations and manage admin access, or Levels 1 and 2 have no content and no safety valve. Present it that way, not as an optional third tier.

---

## 2. Levels redefined

The old Level 2/3 boundary was vague because both touched integration. The clean test is **who starts the conversation, and whether the answer is a fact or a suggestion**.

| Level | Definition | Test | User group | Risk |
| --- | --- | --- | --- | --- |
| **L1 — Public facts** | Information from approved documents. No member data | Could a stranger read this on the website today? If yes, it is L1 | U1, U2 | Low |
| **L2 — My account** | That member's own data, already in the system. **Read-only retrieval** | Is it a fact about *this* person, pulled from a record that exists? If yes, it is L2 | U2 | Low–Medium |
| **L3 — Proactive and promotional** | The bot initiates, or the content is a **suggestion** rather than a fact | Does the bot start it, or tell them to consider something? If yes, it is L3 | U2 | **HIGH** |

Three questions, in order, sort anything:

1. Does it need a login? → separates L1 from L2/L3
2. Is it a fact about this person's record? → L2
3. Does the bot initiate, or suggest? → L3

**L2 is now viable.** BOCIPT's own Customer Services Information lists account balance enquiry via their internet, mobile app and IVRS. So: **viewing stayed with BOCIPT, acting went to eMPF.** A member can see balance, history and statements at BOCIPT; they submit switches, withdrawals and contributions to eMPF, cut-off 4pm.

Caveat for CSI, not for the workshop: their own document says information "may not be updated simultaneously to the trustee's website, mobile apps and IVRS" now that eMPF administers. So balance may lag. Data-freshness question.

---

## 3. Level 3 is the real objective — and the real risk

Elaine's stated objective: as trustee they cannot sell, so **soft promotion bundled with BOCI products** is the value they want, and what they want the regulator to validate.

That is a legitimate sandbox goal. It is also the single thing MPFA will scrutinise hardest. Hold both facts at once.

**Why it is sensitive**

- MPFA Guidelines VI.2 **§III.43**: avoid *predicting, projecting or forecasting* a constituent fund's future or likely performance. General market outlook may be referenced. Fund-level forecasting may not.
- **§III.28**: a *suitability assessment* requires risk profiling, matching fund risk to it, written explanation of why the fund suits the member, the member's signature, and retention for **seven years**. A bot must not do this.
- MPFA's own **Investment Education AI Assistant** (launched 16 June 2026) states its boundary publicly: objective and official information only — **no investment advice, no recommendation of specific schemes or funds, no suitability assessment.**
- Governance Principles for MPF Trustees require trustees to **identify, manage and address conflicts of interest**. A bot on the trustee's official domain nudging members toward BOCI-branded products is a textbook conflict-of-interest question.
- The **Asset Manager** is the entity registered to do MPF sales and marketing. The Trustee is not.

**How to frame it — this is the move**

Do not present L3 as a feature to build. Present it as **the question the sandbox exists to answer**:

> "We want to test with MPFA whether a trustee may surface related BOCI products in a member conversation, and under what conditions. That is exactly what the sandbox is for. We need MPFA's view before this can be specified."

That framing does four things: it is honest, it uses the sandbox for its actual purpose (supervisory engagement), it puts the decision with the regulator rather than with you or CSI, and it protects Elaine internally — she is not signing off on advice-giving, she is asking a question.

**Until MPFA answers, L3 has no requirement.** It cannot be specified, so it cannot be built. Say that plainly. It also means L1 and L2 must stand on their own as a credible October deliverable — which they can.

**Inside L3, separate two things that are not equally risky**

| L3 sub-type | Example | Risk |
| --- | --- | --- |
| **Routing / signposting** | "For this you need eMPF, here is the link" · "Fund switching is done on the eMPF app" · "This is an Asset Manager question" | **Low.** Factual, no recommendation. Ship this. |
| **Factual alert** | "The fund price you set a threshold on crossed it yesterday" | **Medium.** A fact about the past, member opted in. Defensible. |
| **Soft promotion** | "Members often consider…" · bundling BOCI products · any nudge toward a specific fund | **High.** Needs MPFA's view first. |
| **Projection / what-if** | Retirement gap, portfolio simulation, risk analysis | **High.** Permitted only as an illustration with stated assumptions, never a prediction or recommendation. |

Routing is the cheap win hiding inside L3. It costs almost nothing, needs no member data to leave the data centre, and solves the problem created by the June 2025 split — members do not know which of three organisations to ask.

---

## 4. Breaking down Level 1 — the chain

This is what you asked for: scenario → story → information → knowledge base.

Five columns, one row per story:

| Column | Question | Example |
| --- | --- | --- |
| **1. User group** | U1 or U2? | U1 + U2 |
| **2. Scenario / job** | What is the person trying to do, in what situation? | Leaving my job, want to know if I can take my MPF out |
| **3. User story** | As a [who], I want [what], so that [why] | As a member who has left a job, I want to know whether I can withdraw and what to do next, so I do not make a mistake |
| **4. What the bot must say** | The facts, and the boundary | The conditions that permit withdrawal; that the instruction goes to eMPF, not BOCIPT; that BOCIPT cannot advise |
| **5. Knowledge base source** | Which existing document, and who approves it | Their Key Scheme Information Document page "08 When can you withdraw your MPF?" + MPFA guidance. Owner: PS |

**Then two more columns for the requirement pack**

| Column | Question | Example |
| --- | --- | --- |
| **6. What it must NOT say** | The refusal | No advice on whether to withdraw. No tax advice. No prediction of what the balance will be |
| **7. Owner of the task** | BOCIPT / eMPF / Asset Manager | **eMPF** — routing answer only |

Columns 6 and 7 are what CSI needs and what MPFA will ask for. Most requirement packs omit them.

### A ready-made Level 1 knowledge base

BOCIPT already publishes a numbered **Key Scheme Information Document** series on bocpt.com, in plain language. Confirmed pages include:

- 06 How do I manage my MPF when changing jobs?
- 07 When should you adjust your MPF fund choices?
- 08 When can you withdraw your MPF?
- 10 How to make enquiries and complaints?

Plus: Guide to the MPF Scheme, scheme brochures, quarterly fund fact sheets, monthly performance summary, MPF Service Guide, TVC introduction and tips, MPF Consolidation Services.

**These are already written, already approved, already public, and already plain-language.** That is your L1 knowledge base. Do not draft new content. Point at these and ask PS whether the list is complete.

Governance Principle 10 backs this: a trustee *should* communicate clearly, in plain language, free from misleading statements. Using their own published documents is the safest possible source.

### Candidate L1 scenarios to walk through

Each becomes one or more stories:

1. What is MPF and why do I have it
2. Which schemes do you offer, and what is the difference (careful — this edges toward the Asset Manager)
3. I just changed jobs, what happens to my MPF
4. Can I withdraw, and how
5. How do I switch funds / change my allocation
6. What are the fees, and how do they work
7. How has each fund performed (past only)
8. Where do I get a form
9. How do I complain
10. Is this website / message really you (anti-fraud — they publish fake-site warnings)
11. How do I contact you, and what are the hours
12. What is the difference between BOCIPT, eMPF and the Asset Manager

Scenario 12 is the routing story. Scenario 10 is the anti-fraud story. Both are cheap, both hit MPFA's named focus areas, and neither needs member data.

---

## 5. Requirement structure for CSI

Split as you said. Sub-sections to discuss later, but the shape:

**Functional requirements**
- Per user group (U1, U2, U3)
- Per level (L1, L2, L3)
- Per story: what it must say, what it must refuse, who owns the task
- Knowledge base: sources, owners, update process
- Admin console: who can edit, who can review, what gets logged
- Analytics: top questions, unanswered questions, drop-offs
- Escalation: what triggers a human, and who receives it

**Technical requirements**
- On-prem only, no cloud, member data does not leave the data centre
- Language coverage — their site is two languages; CSI staff could not follow Cantonese in the MPFA briefing
- Authentication and permission checks for L2
- Data freshness — the balance-lag caveat above
- Integration points: existing MPF web and app, CIS database, eMPF
- Logging, audit trail, retention
- Model and stack: **CSI chooses, we validate.** Dify and RAGFlow were mentioned; nothing is decided

---

## 6. The decision workshop — frameworks

Your instinct is right: present the idea, the pros and cons, they decide yes or no on the spot. Four frameworks do this properly. Use them together.

### RAPID (Bain) — who decides

Five roles, assigned **per decision**, not per person:

| Role | Meaning |
| --- | --- |
| **R**ecommend | Builds the case, lays out options and trade-offs → **you** |
| **A**gree | Formal veto, but **only on narrow pre-agreed grounds** — Compliance on regulatory grounds, not "I'd have done it differently" |
| **P**erform | Executes after the call → **PS team, CSI** |
| **I**nput | Supplies facts and perspective, cannot block → **frontline staff, Ken, Emily, Cherry** |
| **D**ecide | **One person.** Not a committee |

The two moves that make RAPID work are the **single Decider** and the **scoped Agree**. Most paralysis is an unbounded-veto problem: five people each behave as if they can block, so consensus becomes the floor and nothing ships.

Bain's warning applies directly here: *resist making the most senior person the default Decider.* That recreates the bottleneck. But in your case the CEO will be in the room and this is a company-level call, so the CEO is probably the right D — **write it down and circulate it before the session** so the argument is about the decision, not about who is allowed to make it.

DACI (Driver, Approver, Contributors, Informed) is the simpler version if RAPID feels heavy. Same core idea: one Approver.

### Decision-forcing case — the artifact per candidate

One page per candidate use case. This is what you put in front of them:

1. **Situation** — 3 sentences. What is happening today.
2. **Complication** — 2 sentences. Why it costs them something.
3. **Options** — 2 or 3, **including "do nothing"**. Always include it. It makes the others honest.
4. **Recommendation** — one paragraph, unhedged, with the primary reason.
5. **Risks and mitigations** — 3 bullets maximum.
6. **The ask** — one line, yes/no, with owner and date.

Rules: lead with the recommendation, never bury it. Every claim carries a number, a quote or a source. Last line is always a yes/no ask — never "further analysis needed".

### Weighted scoring — if there are too many candidates

Use this only if you have more candidates than the room can decide by discussion.

- **Fix the criteria and weights BEFORE anyone sees the options.** This is the single highest-leverage rule. Once people can see how their project scores, criteria stop being a measuring instrument and become an argument.
- 4 to 6 criteria. Fewer and everything scores the same. More and the weights get too thin to change an outcome.
- Force weights to sum to 100. A criterion nobody will spend points on is a criterion nobody believes.
- Score **individually and silently**, then discuss only the disagreements.
- 1 to 5 scale, with each level written as an **observable claim**, not an adjective. Everyone must read the same definition of a 4.

Suggested criteria for this project: member value · Elaine's operational number · MPFA sandbox alignment · risk/compliance exposure · buildability in 6 months · data readiness.

Then **MoSCoW** (Must / Should / Could / Won't) to close the October scope.

### Facilitation across hierarchy — the part that decides whether this works

This is your real problem. CEO plus execution-level staff in one room, on an initiative the staff did not ask for. The research is blunt: **the frontline go silent and you get the CEO's guesses instead of their evidence.**

The fix is sequencing, not encouragement:

1. **Silent individual writing first.** Everyone writes on cards alone, in silence, before anyone speaks. Frontline insights get captured before executives frame the conversation.
2. **Then pairs.** Two minutes each.
3. **Then small groups.** Only now does anything reach the plenary.
4. **Leaders speak last.** Ask the CEO explicitly to listen first and share after. Name it out loud as a ground rule — it works better than hoping.
5. **Silent dot voting.** Equal dots for everyone. **Junior staff vote first**, so they are not influenced.
6. **Track who has spoken.** Redirect the dominant. Invite the quiet directly: "Winkie, you handle these calls — what does that look like on a Monday?"
7. **Round-robin with a timer** for anything that needs everyone's view.

Physical setup matters: **circle or mixed small groups, no head of table.** Seating by rank guarantees silence by rank.

Say at the start, out loud: *"Today is a decision session. I will present each option with its trade-offs. You decide yes, no, or later. Nothing goes to the vendor without a decision here."* That converts them from an audience into a decision body — which is what you said you want, and it is also what makes the frontline willing to speak, because their input has a visible consequence.

---

## 7. What to prepare, in order

1. **Confirm the L1/L2/L3 definitions** with Ivy before the workshop, so the room is not learning the vocabulary and making decisions at the same time.
2. **Build the L1 story list** from their existing Key Scheme Information Documents. Twelve candidate scenarios above. One story card each, columns 1–7.
3. **Write a one-page decision case for each L3 candidate**, including "do nothing". L3 is where the decisions actually are.
4. **Write RAPID roles on one line per decision** and circulate before the session.
5. **Agree the scoring criteria and weights in a short separate session** if you expect more candidates than the room can handle by discussion. Ideally with Elaine beforehand, not with the CEO present.
6. **Plan the facilitation sequence** — silent writing, pairs, groups, plenary, leaders last, dot voting.
7. **Get Compliance in the room** for L3, or accept that no L3 decision can be final. Their scoped Agree must be exercised by someone who is actually there.
