# Evidence Schema

Use these schemas when producing structured appendices or reusable research tables.

## 1. Evidence Table

Purpose:

- track important claims
- record evidence quality
- support traceable reporting

Suggested columns:

| Column | Meaning |
| --- | --- |
| information_id | Stable id for the claim |
| information_point | Claim, fact, or conclusion |
| status | fact / inference / unknown |
| source_link | Direct source URL |
| source_level | A / B / C |
| source_type | first-party / official / media / database / repost |
| published_at | Source publish date if available |
| captured_at | Research capture date |
| summary | Short evidence note |
| cross_verified | Y / N |
| related_dimension | background / content / channel / business / timeline / values |
| remarks | conflict, caveat, or extra note |

## 2. Timeline Table

Purpose:

- build chronology before writing interpretation

Suggested columns:

| Column | Meaning |
| --- | --- |
| time | year or year-month |
| event | what happened |
| type | career / content / platform / business / activity / lifestyle |
| impact | why this matters |
| source_link | direct source URL |
| remarks | uncertainty, conflict, or context |

## 3. Content Sample Table

Purpose:

- avoid sampling bias
- track format, topic, and conversion behavior

Suggested columns:

| Column | Meaning |
| --- | --- |
| sample_id | Stable sample id |
| link | Direct URL |
| platform | Where it was published |
| published_at | Publish date |
| content_form | video / article / podcast / live / event page |
| topic_tag | Main topic or series |
| key_point | Main point or claim |
| style_feature | Style or structure note |
| has_conversion_action | Y / N |
| remarks | extra note |

## 4. Business Model Table

Purpose:

- map visible monetization structure
- separate stable revenue from speculative guesses

Suggested columns:

| Column | Meaning |
| --- | --- |
| revenue_type | content / service / product / event / sponsorship / indirect asset |
| product_or_service | Named offer or revenue item |
| pricing_range | Public price or cautious range |
| frequency | one-off / recurring / seasonal / unclear |
| target_user | intended buyer or audience |
| conversion_entry | where the user enters |
| stability | low / medium / high / unclear |
| scalability | low / medium / high / unclear |
| evidence_source | direct source URL or page |
| remarks | uncertainty or additional note |

## 5. Status Guidance

Use `fact` when a public source directly supports the point.

Use `inference` when the point is a reasoned conclusion based on multiple signals or a clearly stated assumption.

Use `unknown` when the available evidence does not justify a conclusion.

## 6. Estimate Guidance

When a table includes estimates:

- state the time range
- show the visible variables
- prefer ranges over single values
- note omitted factors such as taxes, platform cuts, or cost structure
- label it clearly as inference, not fact
