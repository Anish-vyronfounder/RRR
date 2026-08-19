# RRR

RRR — RECOGNIZE • REPAIR • REBUILD

Build a complete, production-quality MVP website for a startup concept called RRR.

Product philosophy

Recognize. Repair. Rebuild.

The product is an AI-powered platform where a normal user can show the system an object/component and choose what they want to do with it.

The user may want to:

identify something

repair something

reuse something

build something from scratch

build something using components they already own

The long-term AI stack will use:

Computer Vision + TensorFlow + RAG + AI reasoning + compatibility engine

The current goal is to build the complete product UI/UX, frontend, pages, components, dashboard, application architecture, database structure, API interfaces, and working MVP flows so the project can later be taken into VS Code for production AI development.

1. IMPORTANT DEVELOPMENT PRINCIPLE

Build the application as a real product, not a landing-page prototype.

The result must have:

complete navigation

functional pages

reusable components

database-ready architecture

API-ready architecture

authentication-ready architecture

image upload workflow

project management

component inventory

document management

AI analysis interfaces

RAG interfaces

repair workflow

reuse workflow

build workflow

identification workflow

Do not create fake buttons that lead nowhere.

Every major UI action should have a working frontend flow or a clearly defined backend/API integration point.

2. VERY IMPORTANT AI ARCHITECTURE

The final system will eventually use:

IMAGE
  ↓
COMPUTER VISION
  ↓
TENSORFLOW
  ↓
OBJECT / COMPONENT IDENTIFICATION
  ↓
STRUCTURED ATTRIBUTES
  ↓
RAG RETRIEVAL
  ↓
TECHNICAL KNOWLEDGE
  ↓
COMPATIBILITY ENGINE
  ↓
AI REASONING
  ↓
REPAIR / REUSE / BUILD RECOMMENDATION


Do NOT pretend a production TensorFlow model already exists.

Instead:

Build clean interfaces for:

vision inference

TensorFlow model integration

RAG query

document retrieval

compatibility checking

AI recommendation

Use realistic demo/mock data where necessary so the application works.

The interfaces must make it easy to replace the mock implementations with real TensorFlow and RAG services later in VS Code.

3. PRIMARY USER EXPERIENCE

When a user opens RRR, the first question should be:

"What do you want to do?"

Show five primary paths:

🔍 Identify

"I want to know what this is."

🔧 Repair

"Something is wrong. Help me fix it."

♻️ Reuse

"I have an old component. What else can I do with it?"

🔨 Build

"I want to build something from scratch."

🧩 Build With What I Have

"I have components already. Help me build something useful."

These five paths are the foundation of the product.

4. VISUAL DESIGN

The UI must use a clean dark-and-white consumer product theme.

The product should feel like a serious modern startup.

Primary colors

black

near-black

charcoal

white

off-white

light gray

Use accent colors sparingly for:

success

warning

error

important actions

DO NOT use:

excessive neon

cyberpunk styling

excessive blue/purple glow

excessive glassmorphism

complicated 3D effects

overly technical industrial dashboard styling

excessive animations

The interface should be understandable to a normal user.

Think:

simple + premium + intelligent + trustworthy

5. LANDING PAGE

Create a premium homepage.

Hero:

RRR

Recognize. Repair. Rebuild.

Supporting text:

Show us what you have. We'll help you understand it, fix it, reuse it, or build something new with it.

Primary CTA:

Start with an image

Secondary CTA:

Explore RRR

Then display the five workflows:

Identify
Repair
Reuse
Build
Build With What I Have

6. IMAGE-FIRST EXPERIENCE

The main interaction should be:

"Show me what you have."

Create a beautiful image upload area.

Support:

drag and drop

file selection

image preview

camera-ready architecture

remove image

analyze image

After upload:

Image
 ↓
Analyzing...
 ↓
Detected Component
 ↓
Attributes
 ↓
Condition
 ↓
Possible Uses
 ↓
Recommended Actions


Create an excellent loading/analyzing experience.

7. IDENTIFICATION RESULT

Create a polished result page.

Example:

WHAT I FOUND

8GB DDR4 RAM

Confidence:

91%

Attributes:

DDR4

8GB

DIMM

Desktop memory

Then:

What is it?

Simple explanation.

Where is it used?

Simple explanation.

What can I do with it?

Upgrade a PC

Build a workstation

Use in a home server

Find compatible systems

Buttons:

Repair

Reuse

Build With This

Add to Inventory

8. REPAIR EXPERIENCE

Create a dedicated repair workflow.

User:

uploads image

describes the problem

optionally uploads manual/document

starts analysis

Result:

WHAT I SEE

Visual observations.

POSSIBLE PROBLEM

Potential issue.

CONFIDENCE

Confidence indicator.

WHAT TO CHECK

Step-by-step diagnostic instructions.

HOW TO REPAIR

Step-by-step repair guidance.

DOCUMENTATION

Retrieved technical documentation.

Important:

Never present uncertain visual inference as absolute fact.

Use wording like:

Possible issue

Visual evidence suggests

Requires testing

Documentation indicates

9. REUSE EXPERIENCE

Create a dedicated reuse page.

Example:

User uploads:

Old RAM

System shows:

IDENTIFIED

8GB DDR4 RAM

POSSIBLE REUSES

Upgrade another compatible PC

Build a workstation

Build a home server

Use as part of a Linux machine

Each recommendation should have:

difficulty

required components

available components

missing components

compatibility status

Button:

Build This

10. BUILD FROM SCRATCH

Create a guided builder.

User chooses:

What do you want to build?

Examples:

PC

home server

electronics project

IoT project

workstation

custom project

Then ask:

budget

purpose

experience level

performance requirements

components already owned

Generate a structured build plan.

Show:

Required Components

Compatible Components

Missing Components

Build Steps

Testing Steps

Documentation

11. BUILD WITH WHAT I HAVE

This should be one of the strongest features.

Create an inventory system.

User can:

upload component image

identify component

save component

enter quantity

add condition

add notes

Example inventory:

8GB DDR4 RAM
500GB SSD
GTX 1650
500W PSU
Intel CPU


Then button:

"What can I build?"

Generate project suggestions.

For every project show:

project name

difficulty

compatible components

missing components

estimated requirements

build steps

12. INVENTORY DASHBOARD

Create:

My Inventory

Cards/table for components.

Each component:

image

name

category

specifications

condition

quantity

compatibility

projects it can be used in

Actions:

edit

delete

view

use in project

13. PROJECT DASHBOARD

Create:

My Projects

Show:

active projects

completed projects

saved projects

recommended projects

Project card:

name

progress

components

difficulty

status

14. AI WORKSPACE

Create the central AI workspace.

Layout:

LEFT

User input / uploaded image

CENTER

Vision result

RIGHT

AI assistant / recommendations

Include:

image

detected component

attributes

confidence

condition

RAG sources

recommendations

compatibility

next actions

This should feel like the main product experience.

15. RAG KNOWLEDGE CENTER

Create a complete frontend for the future RAG system.

Page:

Knowledge

Users can upload:

PDFs

manuals

datasheets

project documentation

text files

markdown files

Show:

document name

type

upload date

processing status

number of chunks

knowledge status

Create:

Search Knowledge

A search interface for asking technical questions.

Example:

"Is this DDR4 RAM compatible with this motherboard?"

Show:

answer

retrieved sources

document names

relevant snippets

confidence

The UI must be designed so the backend RAG system can later provide real retrieval results.

16. RAG ARCHITECTURE INTERFACE

Create API/service interfaces for:

uploadDocument()
processDocument()
queryKnowledge()
retrieveSources()
getRelevantChunks()


Do not hard-code RAG responses into the frontend.

Create a clean service layer.

The real RAG implementation will later be connected from VS Code.

17. COMPUTER VISION INTERFACE

Create a frontend/service abstraction:

analyzeImage()
getDetection()
getAttributes()
getConfidence()
getCondition()


The future TensorFlow model will connect through this layer.

Do not tightly couple the frontend to a temporary model.

18. COMPATIBILITY SYSTEM

Create a compatibility result UI.

Statuses:

✓ Compatible

⚠️ Requires verification

✕ Incompatible

Example:

CPU → Motherboard
✓ Compatible

RAM → Motherboard
✓ Compatible

GPU → PSU
⚠️ Verify power requirements


Create a backend-ready service:

checkCompatibility()
getCompatibleComponents()
getMissingComponents()


The real rule engine will later be implemented in VS Code.

19. DATABASE STRUCTURE

Create database-ready models for:

users

projects

inventory

components

uploaded_images

analyses

recommendations

documents

document_chunks

compatibility_rules

project_components

repair_sessions

reuse_sessions

Design relationships correctly.

Do not put everything into one database table.

20. BACKEND/API STRUCTURE

Create a clean API/service structure for:

/api/vision
/api/rag
/api/repair
/api/reuse
/api/build
/api/inventory
/api/projects
/api/components
/api/documents
/api/compatibility
/api/health


Frontend must use service functions instead of scattering API calls throughout components.

21. AUTHENTICATION

Create a clean authentication flow.

Include:

sign up

login

logout

profile

protected application pages

Keep authentication architecture replaceable.

22. DASHBOARD

Create a beautiful user dashboard.

Show:

Welcome back

Recent analyses

My inventory

Active projects

Saved projects

Recommended projects

Quick actions

Quick actions:

Identify something

Repair something

Reuse something

Build something

Scan my components

23. RESPONSIVE DESIGN

The application must work perfectly on:

desktop

laptop

tablet

mobile

Mobile must not feel like a shrunken desktop.

Make:

buttons touch-friendly

cards responsive

navigation mobile-friendly

upload workflow mobile-friendly

image preview mobile-friendly

24. COMPONENT ARCHITECTURE

Create reusable components.

Examples:

components/
    Navbar
    Sidebar
    Button
    Card
    UploadZone
    ImagePreview
    AnalysisResult
    ConfidenceBadge
    ComponentCard
    InventoryCard
    ProjectCard
    RecommendationCard
    CompatibilityBadge
    SourceCard
    ChatPanel
    StepProgress
    EmptyState
    LoadingState
    ErrorState


Keep components modular.

25. DEMO MODE

The application must run even before the real TensorFlow and RAG backend is connected.

Create:

DEMO MODE

Use realistic sample data.

Example demo:

Upload RAM image

↓

Demo vision response

↓

DDR4 8GB

↓

Demo RAG retrieval

↓

Compatibility check

↓

Reuse recommendations

↓

Build suggestions

The demo must feel like a real product, while clearly separating demo data from production AI.

26. ERROR STATES

Do not ignore errors.

Create polished states for:

failed upload

unsupported image

low confidence

no result

RAG unavailable

API unavailable

document processing

compatibility unknown

empty inventory

empty projects

Example:

"I couldn't confidently identify this component. Try a clearer photo showing the label/model number."

27. LOADING STATES

Create high-quality loading experiences.

Examples:

Analyzing image...

Identifying component...

Searching technical knowledge...

Checking compatibility...

Generating project ideas...

Do not freeze the interface.

28. ACCESSIBILITY

Follow good accessibility practices:

readable contrast

keyboard navigation

semantic HTML

accessible buttons

useful labels

alt text

clear error messages

29. PERFORMANCE

Prioritize performance.

lazy-load heavy pages

optimize images

avoid unnecessary libraries

avoid huge bundles

keep animations lightweight

don't load AI models into the browser unless specifically required

keep AI calls behind service/API boundaries

30. SOURCE CONTROL / EXPORT

Structure the project so it can be exported to GitHub and opened in VS Code.

Keep:

clean source structure

environment variable examples

README

setup instructions

API documentation

database documentation

AI integration documentation

Never hard-code secrets.

31. FINAL ACCEPTANCE TEST

Before considering the project complete, verify:

WEBSITE

✓ Homepage works

✓ Navigation works

✓ Mobile works

✓ Desktop works

✓ Authentication flow works

✓ Dashboard works

IDENTIFY

✓ Upload image

✓ Image preview

✓ Analysis state

✓ Result page

REPAIR

✓ Upload

✓ Problem description

✓ Analysis UI

✓ Diagnostic workflow

REUSE

✓ Component identification

✓ Reuse recommendations

✓ Build action

BUILD

✓ Build wizard

✓ Requirements

✓ Components

✓ Build plan

INVENTORY

✓ Add component

✓ Edit component

✓ Delete component

✓ View inventory

PROJECTS

✓ Create project

✓ View project

✓ Save project

RAG

✓ Upload document

✓ Knowledge interface

✓ Search interface

✓ Source display

AI INTEGRATION

✓ TensorFlow/CV interface exists

✓ RAG service interface exists

✓ Compatibility service exists

✓ Backend/API boundaries exist

✓ Demo mode works

32. MOST IMPORTANT FINAL INSTRUCTION

Do not stop after creating the homepage.

Build the entire product shell and working MVP.

The goal is that when this project is exported into VS Code, we already have:

UI/UX ✓

Frontend ✓

Pages ✓

Components ✓

Dashboard ✓

Database architecture ✓

API architecture ✓

Image workflow ✓

Inventory ✓

Projects ✓

Repair workflow ✓

Reuse workflow ✓

Build workflow ✓

RAG interface ✓

Computer Vision interface ✓

TensorFlow integration point ✓

Compatibility engine interface ✓

Then the next development stage in VS Code will replace the demo implementations with the real:

TensorFlow Computer Vision → high-performance RAG → embeddings → retrieval → reranking → compatibility reasoning → production AI.

Build as much of the complete working product as possible before stopping. Prioritize functional end-to-end flows over decorative features.

This project was built with [Lovable](https://lovable.dev).

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/85a0ac35-4290-4961-863d-e03e67dfd36e).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
