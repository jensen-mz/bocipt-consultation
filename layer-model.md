# Audience and information layer model

## Correction first — you were right about the balance

I over-corrected last time. BOCIPT's own **Customer Services Information** lists *member account balance enquiry* as available through their internet, mobile app, and IVRS channels, and their online dashboard note confirms the landing page after login shows balance, mandate, gain/loss and contribution history.

So the real line is:

> **Viewing stays with BOCIPT. Acting goes to eMPF.**

A member can see their balance, history and statements at BOCIPT. A member submits a switch, withdrawal, transfer or contribution **to eMPF**, cut-off 4pm.

That makes Layer 2 viable after all — the bot can answer "what's my balance" from BOCIPT's own data, not route it away.

**One caveat to check with Cherry or Ken.** Their own document says information "may not be updated simultaneously to the trustee's website, mobile apps and IVRS" after an instruction is processed, because eMPF now does the administration. So BOCIPT's balance may lag. That is a data-freshness question for CSI, not for Elaine. Note it, don't solve it.

---

## Axis A — Audience layers (who is asking)

| Layer | Audience | Login | Volume | Owner of the relationship |
| --- | --- | --- | --- | --- |
| **A1** | Public / non-member | No | Unknown | BOCIPT for facts. **Asset Manager for selling** — they are the registered MPF principal intermediary |
| **A2** | MPF member (My Choice, Easy-Choice) | Yes | ~900,000 accounts | BOCIPT for viewing, complaints, statements. eMPF for transactions |
| **A3** | MPF employer | Yes | Low value now | Administration moved to eMPF in June 2025. Mostly routing |
| **A4** | ORSO employer | Yes | **Unconfirmed — ask** | BOCIPT, end to end. Not on eMPF |
| **A5** | ORSO employee / member | Yes | **Unconfirmed — ask** | BOCIPT, end to end. Not on eMPF |
| **A6** | Beneficiaries, TVC/SVC, personal accounts | Varies | Low | Out of scope per the 2 Oct kickoff. Name them so nobody thinks you forgot |
| **A7** | **BOCIPT's own PS team** | Internal | ~100 staff | **Not an audience layer. See the note below.** |

### Do not call A7 "Layer 3"

This matters, so I will be blunt.

Your PS team is not a third level of the chatbot. They are the **operating layer underneath all of it**. Without them the bot cannot work at any level:

- Somebody has to load and maintain the FAQ, forms and fact sheets → otherwise A1 gets nothing.
- Somebody has to review unanswered questions → otherwise nobody learns what is missing.
- Somebody has to take escalations → otherwise the bot has no safety valve.
- Somebody has to manage admin accounts and access → otherwise it fails audit.

If you present it as "Level 3", two things go wrong. Elaine will think it is optional and can be deferred. And it will collide with the proposal's Level 3, which means something else entirely.

Call it the **Operations layer** or the **Admin console**. Present it as the thing that makes Levels 1 and 2 work, not as a third tier.

That said — it is the layer Elaine's team actually touches every day, so it is the part she will care about most personally. Give it real time in the meeting. Just not the label "Level 3".

---

## Axis B — The proposal's Level 1 / 2 / 3

This is a **different axis**. It measures how sophisticated the bot's behaviour is, not who is asking.

| Proposal level | What it means | Depends on |
| --- | --- | --- |
| **Level 1** | General enquiry. Answers from approved documents. No member data. | Knowledge base + Operations layer |
| **Level 2** | Account enquiry after login. Reads that member's own data. Read-only. | Level 1 + authenticated data access |
| **Level 3** | Proactive guidance, simulation, alerts, projections. The sandbox stretch. | Level 2 + Compliance sign-off on the advice boundary |

### How the two axes cross

|  | **Level 1** — general | **Level 2** — account | **Level 3** — guidance |
| --- | --- | --- | --- |
| **A1 Public** | ✅ Natural fit. Scheme facts, fund facts, how to complain, scam check | — cannot, no login | Marketing-led. Asset Manager's call, not the Trustee's |
| **A2 MPF member** | ✅ Same content, plus logged-in context | ✅ **Now viable** — balance, gain/loss, history, statements from BOCIPT's own data | ⚠️ Projections, alerts, gap analysis. Advice boundary |
| **A3 MPF employer** | ✅ Routing answers | Mostly eMPF's | — |
| **A4/A5 ORSO** | ✅ | ✅ **Cleanest case — BOCIPT owns everything, no eMPF split** | ⚠️ Same boundary |
| **A7 PS team** | Operates the knowledge base | Reviews conversations, handles escalations | Reads the analytics |

**The useful insight:** ORSO at Level 2 is the only cell with **no ownership conflict at all**. BOCIPT owns the whole operation. No eMPF boundary, no Asset Manager overlap. If Elaine's ORSO team is drowning in repeated questions, that is the cleanest place to prove the bot works. Low volume though — MPFA wants member engagement at scale. Ask her, don't decide.

---

## Axis C — Information layers (what content)

Your four, corrected and split. Layer 3 had to be split because one half is permitted and one half is not.

| Layer | Content | Login | Risk | Evidence |
| --- | --- | --- | --- | --- |
| **I1 — Facts** | Scheme information, fund facts, **past** performance, fees, fund manager info, how to complain, how to verify a site is genuine | No | **Low** | Already public on bocpt.com. MPFA's Disclosure Code requires fee tables and cost illustrations anyway. Governance Principle 10 positively *requires* clear plain-language communication |
| **I2 — My account** | Balance, gain/loss, contribution history by fund and by source, mandate, statements, fund prices | Yes | **Low–Medium** | Already on their dashboard. Risk is permission and freshness, not content |
| **I3a — Factual alerts** | A member sets a threshold; the bot tells them a **past** price crossed it | Yes | **Medium** | Fund price history already exists. It is a notification, not a view about the future |
| **I3b — Interpretation** | "The HK market is rising so these funds may benefit", what-if projections, retirement gap, risk analysis, portfolio recommendation | Yes | **HIGH** | MPFA Guidelines VI.2 §III.43: avoid *predicting, projecting or forecasting* a fund's future or likely performance. §III.28: a suitability assessment requires risk profiling, matching, written explanation, member signature, 7-year retention. **A bot must not do this** |
| **I4 — Routing** ⭐ | "This task belongs to eMPF / to BOCIPT / to the Asset Manager — here is how to reach them" | No | **Low** | The gap created by the June 2025 split. **You did not have this layer. It is the highest-value one.** |
| **I5 — Operations** | Knowledge base maintenance, unanswered-question review, escalation queue, analytics, admin access | Internal | **Low** | The Operations layer. Prerequisite for everything above |

### Why I4 is the one to push

Since 5 June 2025 a member's journey runs through **three organisations**, and members do not know which one to ask. BOCIPT's own site tells them to stop submitting instructions to BOCIPT — and BOCIPT still gets the calls.

I4 is cheap, low-risk, needs no member data to leave the data centre, and is easy to measure: misrouted calls fall. It hits two of MPFA's three sandbox focus areas — customer experience and operational efficiency — and can be built while I3b is still being argued about by Compliance.

Ask Elaine: **"How many of your calls are people who should have called 183 2622?"** If the number is large, this is your first use case and you have your October story.

### The line MPFA already drew for you

MPFA launched its own **MPF Investment Education AI Assistant** on 16 June 2026. Its published boundary: *objective and official information only — no investment advice, no recommendation of specific schemes or funds, no suitability assessment.*

That is the regulator's own chatbot, same theme, line already drawn in public. If BOCIPT's bot stays inside it, the project is defensible by definition. Show Elaine that boundary and ask her to mark where her own line falls. **Do not draw it for her** — that is a PS and Compliance decision, and getting them to own it is the point.

Safe zone: **facts yes, navigation yes, routing yes, factual alerts yes, illustration with stated assumptions yes.** Not safe: **advice, recommendation, suitability, forecasting.**

---

## The competitor gap

Four MPF providers already have AI member tools. **All four are advisory/robo, and none built it in-house.**

| Provider | Tool | Built with |
| --- | --- | --- |
| BCT | MARIO — AI advisor, portfolio recs, chatbot, quarterly nudges | AQUMON |
| Manulife | MPF Robo-Advisor — portfolio insights, fund-level advice | AutoML Capital + Syfe |
| Sun Life | MPF Navigator — 5-question risk profile, 5 reference portfolios | AQUMON |
| AIA | MPF Smart Advisor — 50 portfolios, simulate without switching, gap calculator | Magnum Research / AQUMON |
| MPFA | Investment Education AI Assistant — info only, no advice | — |

No comparable tool found from HSBC or Hang Seng. Their BT team already looked at these and called the MPFA one broken.

**Nobody has built the service-and-routing bot.** Everybody went for advice, which needs a suitability framework and a fintech partner. That route is not achievable in six months and is not what BOCIPT's submission describes.

**BOCIPT's defensible lane:** authoritative facts + my-account retrieval + routing to the right owner + anti-fraud verification. Aligns with MPFA's own boundary rather than competing with it.

---

## Presenting this to Elaine — diagram options

I searched for how to present layered audience and content models. Three patterns fit, and they do different jobs. My recommendation is **two graphics, not one.**

### Recommended: the matrix (main graphic)

Rows = audience (A1–A5). Columns = information layer (I1, I2, I3a, I3b, I4). Each cell marked **in / later / no**.

Why it works: it is the standard audience-matrix pattern, and it does three things at once — shows coverage, shows gaps, and forces a decision per cell. Elaine can point at a cell and say "not that one". That is exactly what you need. It also becomes your October scope document with almost no extra work.

The advice boundary shows up naturally as a vertical line: everything left of I3b is safe, I3b is the contested column.

### Supporting: the ownership boundary strip

Three columns — **BOCIPT | eMPF Platform | Asset Manager** — with member tasks placed in each. One visual that explains I4 without you having to say a word about it.

This is the graphic that makes the "routing" use case obvious. Once she sees how split her members' journey is, the value of I4 explains itself.

### Not recommended for Elaine

- **Concentric / onion layers** (public → member → staff). Looks elegant but hides the ownership problem, which is the most important thing in the room.
- **Swimlane process diagram.** Right tool for CSI and for the workshop itself, wrong tool for a first conversation with an operations head. Too much detail too early.

Save the swimlane for Monday's workshop, where you draw the member's journey left to right and mark failure points.

---

## What to ask Elaine to fill this in

1. "Who does this bot serve — MPF members only, or ORSO too?"
2. "How much of your team's time goes to ORSO employers and members?" → decides whether A4/A5 get a slot
3. **"How many of your calls are people who should have called 183 2622?"** → sizes I4, your best use case
4. "Can members see their balance with you, or only on eMPF now?" → confirm the view/act split from her side
5. "Is that balance always current, or does it lag?" → the freshness caveat
6. "Which of these does your team answer most often?" — then put I1–I4 in front of her in plain words, not as slides
7. "Do members ask for things that are **not** on the portal today?" → your Layer-2 gap question
8. "On projections and alerts — where is your line between an illustration and advice? Who decides?" → get a **name**, not an answer
9. "Have you seen BCT's MARIO, or what Manulife and AIA did? What did you think?" → how ambitious she wants to be
10. "Who on your team would own the knowledge base day to day?" → the Operations layer needs a named person or it will not survive

---

## Still unconfirmed

- ORSO client and member counts — nothing public
- Whether ~900,000 accounts and 5th-by-AUA are still current (end-2023 figures)
- Whether the 7.4% / 6th place from the kickoff is a different metric or a different year — ask, don't assert
- How fresh BOCIPT's balance data is now that eMPF does the administration
