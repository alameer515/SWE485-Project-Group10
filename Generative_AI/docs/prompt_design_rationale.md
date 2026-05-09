# Prompt Design Rationale
## Phase 2 – Generative AI Integration

## Overview

This document explains the thinking behind each prompt template we designed for integrating Generative AI into our clothing size recommendation system. It covers how domain knowledge shaped our design decisions, what we learned from the process, and references to prompt engineering practices we followed.

## Background

Our system uses a Random Forest classifier trained on the Clothing Fit Dataset to predict whether a clothing item will be a **Fit**, **Small**, or **Large** for a given customer. The generative AI layer takes that prediction and translates it into natural language advice.

The core challenge in prompt design for this project was: how much context does the model actually need to give useful, accurate advice? We structured our four templates to answer that question progressively, starting from minimal input and building toward full context.

## Template 1 – Basic Prediction Explainer

### Thought Process

The first thing we needed was a baseline. Before adding any user data, we wanted to know how well a language model can explain a fit prediction on its own, with just the label as input. This forces the model to work from general knowledge about clothing fit rather than anything user-specific.

We kept the instruction deliberately short and restricted it: "explain what this means, don't suggest action." The reason for that restriction is that without any user data, any action the model suggests would be a guess. We'd rather have a clean explanation than a confident-sounding but irrelevant recommendation.

### Domain Knowledge Influence

In the clothing domain, the terms "fit," "small," and "large" as *fit labels* (not size labels) can confuse users. A "Large" fit prediction means the item runs large — not that the customer is large. This distinction mattered when writing the prompt. We explicitly framed it as "the system predicted that a 'Large' fit label applies" rather than "the customer is Large" to avoid generating offensive or misleading output.

### Limitations Identified

After writing this template, it became clear that the output would be nearly identical for every user with the same label. It's informative but impersonal. This limitation directly motivated the design of Templates 2 and 3.

### Lessons Learned

Testing this template showed that it works well as a simple baseline for explaining the prediction label. The responses were usually short and easy to read, but they were also very generic because the model only received the predicted fit label without any customer-specific context.

We also observed that this template could sometimes misinterpret labels such as "Small" or "Large" as descriptions of the customer rather than descriptions of how the item fits. This highlighted the importance of clear prompt framing in the clothing-fit domain.

Overall, this template was useful for establishing a baseline, but it showed clear limitations in personalization and consistency.

## Template 2 – Measurement-Aware Personalized Advice

### Thought Process

The dataset has good coverage of customer body attributes: height, weight, and other measurements. These are exactly the variables our Random Forest model uses to make predictions, so it makes sense to pass them to the language model as well. The idea is that if the model knows why the prediction was made (based on these measurements), it can explain it more accurately and personally.

We chose to list the attributes as a structured profile rather than embedding them in prose. This format (bullet list inside the prompt) is easier for the model to parse and less likely to cause it to lose track of individual values when generating a response.

### Domain Knowledge Influence

Body type was an important field to include because it captures shape beyond just height and weight. For example, two customers with the same height and weight but different body types (athletic vs. pear-shaped) would have very different fit experiences, especially in bottoms like jeans or skirts. Including body type allows the model to tailor advice to shape rather than just size.

Age was included because it can correlate with fit preferences (e.g., older customers sometimes prefer a looser fit), though we acknowledge this is a soft signal and the model may not always use it meaningfully.

### Lessons Learned

From testing this template, we observed that including user measurements significantly improved the personalization of the responses. Compared to Template 1, the advice was more relevant to the customer profile and better aligned with the idea of a personalized recommendation system.

At the same time, we noticed that the model sometimes made assumptions that went slightly beyond the given input, such as confidently recommending a different size even when the prediction alone did not fully justify that recommendation. This showed that adding more context improves usefulness, but it can also encourage the model to be more assertive than intended.

Overall, this template demonstrated that structured measurement input is valuable, but the wording must still be carefully controlled to avoid overconfident advice.



## Template 3 – Cluster-Informed Contextual Advice

### Thought Process

This template was designed specifically to bridge the unsupervised learning component (Part A) with the generative AI component. The clustering step in Part A groups customers with similar characteristics, and those groups capture patterns that individual measurements alone may not express — for example, a cluster of customers who consistently report that certain brands run large for them.

Rather than passing a raw cluster ID (which means nothing to the model), we pass a human-readable description of the cluster profile. This description is written based on our cluster analysis and captures the key characteristics of that group in plain language.

The prompt then asks the model to reflect on what customers in that group commonly experience — which encourages it to generalize across the group rather than just interpreting one individual's numbers.

### Domain Knowledge Influence

In e-commerce, shopper segments are a well-established concept. Retailers like Amazon already use customer profiles to personalize recommendations. Our cluster descriptions mirror this approach: instead of just saying "Cluster 2," we describe it as "shorter customers under 163 cm who frequently report items running large." This kind of language is grounded in how fashion retailers actually communicate about their customers internally.

### Lessons Learned

This template showed that adding cluster-level context can make the generated advice more informative and more connected to the unsupervised learning part of the project. Using a human-readable cluster description helped the model produce responses that felt more context-aware than those of the simpler templates.

However, the results also showed that output quality depends heavily on the quality of the cluster description itself. When the cluster profile was clear and meaningful, the response was stronger; when it was vague, the generated advice became less useful.

This taught us that clustering can improve Generative AI outputs, but only when the cluster interpretations are written in a clear and informative way.


## Template 4 – Actionable Shopping Guide

### Thought Process

Templates 1–3 are all explanatory — they tell the user what the prediction means. Template 4 goes a step further and tells the user what to *do*. It adds two new fields that the other templates lack: the clothing category and the brand.

We added these because sizing varies significantly by both category and brand. A customer who usually wears a medium top might need a large in jeans from the same brand, and might need a small in tops from a different brand entirely. The model's general knowledge about brands and categories lets it add a practical tip that goes beyond what our dataset alone can provide.

The structured instruction ("1. Explain, 2. Suggest size, 3. Give a tip") was chosen deliberately. Without explicit structure, language models tend to either blend all three into one run-on paragraph or omit one of them. By numbering the required outputs, we get consistently organized responses that are easier to evaluate.

### Domain Knowledge Influence

This template was the most influenced by domain knowledge. We thought about what a knowledgeable salesperson in a physical store would say when helping a customer: they would acknowledge the issue, tell you what to pick instead, and maybe share something specific they know about that brand. Template 4 tries to replicate that experience in text.

The friendly and direct tone instruction at the end was added because early drafts of this template produced overly formal or hedged responses. In a retail context, that tone feels off-brand.

### Lessons Learned

This template produced the most detailed and practical responses during testing. The structured instructions helped the model generate outputs that were more organized, including explanation, recommendation, and an actionable shopping tip.

At the same time, the added structure sometimes made the model sound overly confident, especially when suggesting what size to try next. This means that while explicit instructions improve consistency and usefulness, they can also increase the risk of overgeneralization.

Overall, this template demonstrated the value of structured prompting for user-facing advice, but it also showed the need to balance helpfulness with caution.



## References to Prompt Engineering Best Practices

The following principles from established prompt engineering guides informed our design:

- **Be specific about format and length**: All four templates specify the desired output length (e.g., "2-3 sentences"). This reduces variance in output and makes outputs easier to compare. *(Source: OpenAI Prompt Engineering Guide)*

- **Use structured input for structured data**: Template 2 uses a bullet-list format for customer attributes rather than embedding them in prose. This reduces the chance of the model misreading numerical values. *(Source: Anthropic Prompt Engineering Documentation)*

- **Separate explanation from action**: Templates 1 and 3 deliberately restrict the model to explanation only. This principle of task isolation helps produce cleaner, more focused outputs when you don't need the model to do everything at once. *(Source: Google DeepMind prompting best practices)*

- **Increase context progressively**: Our four templates form a progression from minimal (T1) to full context (T4). This is a standard technique for ablation-style prompt evaluation, by varying one element at a time, you can isolate which context actually helps.

- **Avoid ambiguous framing**: The distinction between "fit label" and "size" was addressed explicitly in all prompts to prevent the model from confusing the two concepts. Ambiguous framing is one of the leading causes of off-topic or misleading LLM outputs.