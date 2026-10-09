# Internal user — requirements and user stories

Module owner: me. Covers the people who run the bot, not the members who use it.

---

## Roles

**PS Admin** — Pension Services officer. One of roughly 100 staff, mostly officer grade. Owns member-facing content and is accountable for what the bot says. Not technical. Works in gaps between call volumes, so anything that needs a ticket will not happen.

**IT Admin** — Business Technology. Supports the platform, not the content. Needs enough visibility to troubleshoot. Must not be able to change what members are told. Holds account provisioning and revocation.

### Access matrix

| Capability | PS Admin | IT Admin |
| --- | --- | --- |
| Knowledge base — add, edit, enable, disable, delete | **Full** | **Read only** |
| Activity log | View | View and export |
| Playground and golden test set | **Full** | View |
| Conversations and analysis | **Full** | View |
| Provision / revoke PS Admin accounts | No | **Yes** |
| System prompt, model temperature, agent building blocks | **No — locked** | **No — locked** |
| Guardrail and refusal rules | **No — vendor configured** | **No — vendor configured** |

---

## Module 1 — Knowledge base management (MUST HAVE)

The bot answers only from what is loaded here. Nothing else feeds it.

**Story 1 — Bulk upload** · `Must have` · PS Admin

> I'm the PS officer who has been given ownership of the chatbot content, on top of my normal queue of calls and counter work. I've been handed a folder of approved documents — scheme guides, fact sheets, forms — and I have maybe an hour between shifts to deal with it.
>
> I want to upload the whole folder at once and have it become the bot's knowledge.
>
> I need it to tell me which files worked and which didn't, and let me retry just the failures — because if one bad file kills the whole upload, I won't have time to start again.

**Story 2 — Add a single entry** · `Must have` · PS Admin

> I'm a PS officer. A member rang this morning asking something none of our documents actually cover. I know the answer, but there's nothing in the library for the bot to find.
>
> I want to type one question and answer in myself and publish it.
>
> I need it to warn me if something near-identical is already in there, because the last thing I want is two entries saying slightly different things and not knowing which one the bot picked.

**Story 3 — Edit** · `Must have` · PS Admin

> I'm a PS officer and a scheme rule changed. There's an entry in the library that was right last month and is wrong today.
>
> I want to open it, fix the wording and save.
>
> I need the bot to use the new text straight away, and I need it to tell me if a colleague changed the same entry while I had it open — I can't have two of us overwriting each other and neither knowing.

**Story 4 — Disable without deleting** · `Must have` · PS Admin

> I'm a PS officer and I've just realised one of our answers is wrong and members are reading it right now.
>
> I want to switch that entry off immediately.
>
> I need it to stop being used the moment I press the button, not at the next overnight rebuild — and I need the content kept, because I'll be correcting it in ten minutes, not rewriting it from scratch.

**Story 5 — Restore a disabled item** · `Must have` · PS Admin

> I'm a PS officer. I disabled an entry yesterday in a panic, and it turned out the content was fine — the problem was somewhere else.
>
> I want to switch it back on.
>
> I need it to warn me if the source document has been replaced since I turned it off, because restoring something out of date is worse than leaving it off.

**Story 6 — Delete permanently** · `Must have` · PS Admin

> I'm a PS officer and a scheme has been withdrawn. The content should never be shown to a member again.
>
> I want to delete it for good.
>
> I need it to make me confirm, and to say plainly that I can't undo it — if it's live and being used, I want a second warning before it goes.

**Story 7 — Categories** · `Must have` · PS Admin

> I'm a PS officer and the library is going to have a few hundred items in it once everything is loaded.
>
> I want to file each item under a category — scheme information, forms, fund facts, complaints, member guidance.
>
> I need every item to have one, because an uncategorised library is one I stop trusting and start avoiding.

**Story 8 — Search and filter** · `Must have` · PS Admin

> I'm a PS officer about to write a new entry, and I don't want to duplicate something that already exists.
>
> I want to search the library by category, status, language and keyword.
>
> I need it to search inside the content, not just the titles — our titles are document names, and members don't ask questions using document names.

**Story 9 — Status view** · `Must have` · PS Admin

> I'm a PS officer with an hour a week to look after this.
>
> I want one screen that tells me what's live, what's disabled, what's waiting for review and what's missing a language version.
>
> I need to see the gaps without opening every item one by one, because I won't do that.

**Story 10 — Superseded flag** · `Must have` · PS Admin

> I'm a PS officer. Our fund fact sheets come out every quarter, which means four times a year a chunk of the library quietly goes out of date.
>
> I want to upload the new fact sheet and have everything sourced from the old one flagged for review.
>
> I need those flagged items listed together, and I need to see the flag in the status view — because otherwise the bot keeps answering from last quarter's numbers and nobody notices until a member complains.

**Story 11 — Scheduled publication** · `Must have` · PS Admin

> I'm a PS officer. Quarterly updates have an effective date, and that date is not always a day I'm free.
>
> I want to load the content now and set the day it goes live.
>
> I need to be able to cancel or move that date before it fires, because effective dates do change.

**Story 12 — Language versions** · `Must have` · PS Admin

> I'm a PS officer and our members read us in English, Traditional Chinese and Simplified Chinese.
>
> I want to see, for each entry, which of the three exist and which are missing.
>
> I need it to stop me publishing something English-only and assuming it will serve a Chinese-speaking member — that has to be a decision I make deliberately, not something that happens by accident.

---

## Cross-cutting — activity log and access control (MUST HAVE)

A log only means something if accounts belong to a named person. See open item 2.

**Story 13 — View the activity log** · `Must have` · PS Admin

> I'm a PS officer and Compliance has asked me why the bot gave a member a particular answer three weeks ago.
>
> I want to open that entry's history and see every change to it.
>
> I need the named person, the timestamp, and what it said before and after — and I need to know nobody can edit or delete that history, including me.

**Story 14 — Export the activity log** · `Must have` · IT Admin

> I'm IT Admin and I have to keep audit records outside the chatbot system.
>
> I want to export the log for a date range.
>
> I need everything in that range, including failed and rejected attempts — a log that only records what succeeded isn't an audit trail.

**Story 15 — PS Admin authority** · `Must have` · PS Admin

> I'm a PS officer, not an IT person. If every content change needs a ticket, the content will not get changed.
>
> I want to manage the knowledge base, the testing and the conversation review myself.
>
> I need it to work without another approval step — and I need it to be clear that the system prompt, the model settings and the refusal rules are not mine to touch, so nobody thinks I can quietly change how the bot behaves.

**Story 16 — IT Admin read only on knowledge** · `Must have` · IT Admin

> I'm IT Admin and I get pulled in when something breaks.
>
> I want to read the knowledge base and its history so I can work out what happened.
>
> I need every add, edit, enable, disable and delete control to be unavailable to me — and I need that enforced on the server, not just hidden in the interface, because a support account that can change what 900,000 members are told is an incident waiting to happen.

**Story 17 — IT Admin visibility of testing and conversations** · `Must have` · IT Admin

> I'm IT Admin and a PS colleague has reported that an answer looks wrong.
>
> I want to open the playground and the conversation records to see it for myself.
>
> I need read-only access — I must not be able to alter the golden test set or a saved baseline, or my troubleshooting becomes the reason the numbers stopped meaning anything.

**Story 18 — Provision and revoke** · `Must have` · IT Admin

> I'm IT Admin and people join and leave Pension Services.
>
> I want to grant and revoke PS Admin access by name.
>
> I need it to take effect immediately and be recorded — including cutting off a session that's already open, because someone's last day is their last day. And a PS Admin must not be able to make another PS Admin; that's my job, not theirs.

---

## Module 2 — Playground and automated testing (GOOD TO HAVE)

**Pending:** unknown whether their vendor can deliver this. The bot runs without it.

**Story 19 — Test before publishing** · `Good to have` · PS Admin

> I'm a PS officer and I've just edited an entry that members will see.
>
> I want to type the question in a private playground and see what the bot would actually say.
>
> I need those test conversations kept out of the real conversation records — if my own testing turns up in the analysis, the numbers I report to management are wrong.

**Story 20 — See the source** · `Good to have` · PS Admin

> I'm a PS officer and the bot gave a wrong answer.
>
> I want to see which knowledge item produced it, and which part of it.
>
> I need it to tell me clearly when nothing matched at all — otherwise I'll spend an hour fixing a document that wasn't the problem.

**Story 21 — Golden test set** · `Good to have` · PS Admin

> I'm a PS officer. There are maybe thirty questions we must always get right, and I want to know if we still do.
>
> I want to keep that list and its expected answers in one place.
>
> I need the expected answer recorded as a meaning, not as exact wording — if I have to match the sentence character for character, every harmless rephrasing looks like a failure and I'll stop trusting the report.

**Story 22 — Run and compare** · `Good to have` · PS Admin

> I'm a PS officer and I've just changed something.
>
> I want to run the golden set and compare it against the last known-good result.
>
> I need it to tell me *which* questions changed, not just how many — a count of four doesn't tell me whether to publish or stop.

**Story 23 — Regression report** · `Good to have` · PS Admin

> I'm a PS officer and I edited one entry, but the bot's answers come from the whole library.
>
> I want to see the before and after answer for every question affected by my edit.
>
> I need to catch the damage before a member does, because I can't review every answer by hand.

**Story 24 — Approve a new baseline** · `Good to have` · PS Admin

> I'm a PS officer and the change I just made was deliberate — the new answer is the better one.
>
> I want to accept the current results as the new baseline.
>
> I need my name on that approval, and I need it to be a PS Admin action only — if IT can approve a baseline, the baseline stops being evidence of anything.

---

## Module 3 — Conversation review and analysis (GOOD TO HAVE)

**Pending:** same vendor question as Module 2. This module is also the strongest part of the story to the regulator, because it shows a closed loop rather than a static bot.

The unanswered queue is the point of this module. Members ask, the bot cannot answer, PS Admin sees the gap and writes the content, the next member gets an answer. Without that loop this module is only a log viewer.

**Story 25 — Search conversations** · `Good to have` · PS Admin

> I'm a PS officer and a member has complained about something the bot told them.
>
> I want to find that conversation by keyword, date or topic.
>
> I need to read the whole exchange, not a summary — I have to know exactly what was said before I can respond to the complaint.

**Story 26 — Export conversations** · `Good to have` · PS Admin

> I'm a PS officer and I've been asked for material for a management or regulator report.
>
> I want to export a filtered set of conversations.
>
> I need the export itself recorded — who took what and when — because these files contain member data.

**Story 27 — Top questions** · `Good to have` · PS Admin

> I'm a PS officer and I want to know what members are actually struggling with, rather than what I assume they're struggling with.
>
> I want the most common questions for a period, ranked, with examples under each.
>
> I need them grouped by meaning — people phrase the same question fifty different ways, and if it only counts identical wording it will tell me nothing.

**Story 28 — Unanswered queue** · `Good to have` · PS Admin

> I'm a PS officer and every question the bot couldn't answer is a document I haven't written yet.
>
> I want those questions as a ranked to-do list.
>
> I need refusals kept in a separate list from genuine gaps — when the bot correctly declines to give investment advice, that's not missing content, that's the guardrail working. If the two are mixed I'll be told to write content that Compliance has forbidden. And I do want to see the refusals on their own, because members repeatedly pushing at the same boundary is something MPFA would want to know about.

**Story 29 — Close the loop** · `Good to have` · PS Admin

> I'm a PS officer looking at the unanswered queue, and I can see the same question being asked forty times a week.
>
> I want to create a knowledge item straight from that question.
>
> I need the member's own wording carried across, the original question linked to the new entry, and the queue to shrink when I've filled it — because if I have to retype it and can't see the progress, I won't keep doing it.

**Story 30 — Usage reporting** · `Good to have` · PS Admin

> I'm a PS officer and I have to justify this project to my management and to the regulator.
>
> I want conversation volume, sessions and the answer rate for any period.
>
> I need it exportable, because it's going into someone else's document.

**Story 31 — Member data in conversation records** · `Good to have` · IT Admin

> I'm IT Admin. If members can ask about their own account, these conversation records will contain their personal data.
>
> I want to be able to troubleshoot without reading data I have no reason to see.
>
> I need identifiers masked or withheld unless there's a recorded reason — and I need that rule set by the client and Compliance, not decided by whatever the vendor's product does by default.

---

## Non-functional requirements

Not user stories. Constraints on the solution design.

- **Guardrails are configured by the vendor at build time.** The client supplies the rules — no advice, no fund recommendation, no performance forecasting, no suitability assessment. Users cannot edit these in the portal. The client owns the rules; the vendor owns the implementation.
- **System prompt, model temperature and agent building blocks are locked.** Not user-editable, therefore not versionable by users. This is why there is no versioning or rollback story anywhere in this pack.
- **No human escalation.** The bot answers or states that it cannot. There is no handoff to a person anywhere in this design.
- **All data on premise.** Conversation records, knowledge and logs stay in their data centre. Nothing goes to the cloud.
- **Authorisation is enforced server side.** Hiding a control in the interface is not access control. Every restriction in these stories must be tested by calling the API directly with the wrong role.
- **Retention and audit.** Conversation records and the activity log must be retained and exportable. Retention period to be confirmed by Compliance.

## Out of scope

- Human escalation or handoff
- Versioning and rollback of model or prompt configuration
- Guardrail editing in the portal
- Member-facing features — covered by the L1 / L2 / L3 workstream

---

## Open items

1. **Multilingual embedding.** Their site is English, Traditional Chinese and Simplified Chinese. Not a feature — a technical decision that affects how knowledge is indexed and searched. Confirm before CSI designs retrieval. Story 12 assumes it.
2. **SSO and RBAC.** The activity log is only meaningful if accounts are attributable to a named person. Confirm whether SSO is available or accounts are local. Without this, stories 13, 14 and every restriction in this pack are unverifiable.
3. **Vendor capability for Modules 2 and 3.** Both are pending. Confirm with CSI early. If neither is deliverable, the October story rests on Module 1 alone plus conversation export.
4. **Retention period** for conversation records — Compliance to confirm.
5. **Who is the PS Admin.** A named owner, or the library will drift. Roughly 100 staff in Pension Services, mostly officer grade, so this has to be a specific person, not a team.
6. **Member data in conversation records.** If Level 2 is live, conversations will contain member personal data. Who may read them, and in what form, is a Compliance decision — not something for the vendor to assume.
