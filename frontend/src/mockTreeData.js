const mockTreeData = [
  {
    "name": "Marketing",
    "description": "Purpose related to strategizing and executing marketing initiatives.",
    "transformations": "[\"BLUR\", \"REMOVEBG\"]",
    "parent_id": null,
    "selected": false,
    "purpose_id": 1
  },
  {
    "name": "Offline",
    "description": "Tailored for traditional marketing channels that do not require internet access.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 1,
    "selected": false,
    "purpose_id": 2
  },
  {
    "name": "Print Advertising",
    "description": "Specifically aimed at marketing efforts through printed materials.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 2,
    "selected": false,
    "purpose_id": 3
  },
  {
    "name": "Outdoor Advertising",
    "description": "Perfect for organizing and managing billboard and other forms of outdoor promotions.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 2,
    "selected": false,
    "purpose_id": 4
  },
  {
    "name": "Event Marketing",
    "description": "Geared towards promoting and managing events for marketing purposes.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 2,
    "selected": false,
    "purpose_id": 5
  },
  {
    "name": "TV and Radio Advertising",
    "description": "Suited for advertising campaigns through television and radio channels.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 2,
    "selected": false,
    "purpose_id": 6
  },
  {
    "name": "Online",
    "description": "Purpose revolving around internet-based marketing tactics.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 1,
    "selected": false,
    "purpose_id": 7
  },
  {
    "name": "Social Media",
    "description": "Specifically for navigating the rapidly changing landscape of social media.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 7,
    "selected": false,
    "purpose_id": 8
  },
  {
    "name": "LinkedIn",
    "description": "Custom-built for exploiting LinkedIn's professional network for marketing opportunities.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 8,
    "selected": false,
    "purpose_id": 9
  },
  {
    "name": "Instagram",
    "description": "Designed for utilizing Instagram's visual-heavy platform for marketing strategies.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 8,
    "selected": false,
    "purpose_id": 10
  },
  {
    "name": "Facebook",
    "description": "Tailored for leveraging Facebook's vast user base for targeted marketing.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 8,
    "selected": false,
    "purpose_id": 11
  },
  {
    "name": "Website",
    "description": "Intended for improving and maintaining website for better online presence.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 7,
    "selected": false,
    "purpose_id": 12
  },
  {
    "name": "HR",
    "description": "Designed for all facets of managing human resources.",
    "transformations": "[]",
    "parent_id": null,
    "selected": false,
    "purpose_id": 13
  },
  {
    "name": "Recruitment",
    "description": "Geared towards the streamlined and effective process of recruiting talent.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 13,
    "selected": false,
    "purpose_id": 14
  },
  {
    "name": "Payroll Processing",
    "description": "Suited for the regular task of managing and executing payroll.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 13,
    "selected": false,
    "purpose_id": 15
  },
  {
    "name": "Training and Development",
    "description": "Tailored for the continuous process of enhancing employees' skills.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 13,
    "selected": false,
    "purpose_id": 16
  },
  {
    "name": "Performance Evaluation",
    "description": "Designed for the structured process of assessing employee performance.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 13,
    "selected": false,
    "purpose_id": 17
  },
  {
    "name": "Sales",
    "description": "Intended for all sales-related operations and strategies.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": null,
    "selected": false,
    "purpose_id": 18
  },
  {
    "name": "Customer Relationship Management Access",
    "description": "Custom-built for maintaining healthy customer relations and database access.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 18,
    "selected": false,
    "purpose_id": 19
  },
  {
    "name": "Sales Order Processing",
    "description": "Geared for efficiently processing orders to improve sales operations.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 18,
    "selected": false,
    "purpose_id": 20
  },
  {
    "name": "Sales Campaign Management",
    "description": "Tailored for running effective sales campaigns.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 18,
    "selected": false,
    "purpose_id": 21
  },
  {
    "name": "Sales Forecasting",
    "description": "Geared towards predicting and strategizing future sales.",
    "transformations": "[\"BLACKWHITE\"]",
    "parent_id": 18,
    "selected": false,
    "purpose_id": 22
  },
  {
    "name": "Microsoft 365",
    "description": "Aimed at efficient utilization of Microsoft 365 for various tasks.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": null,
    "selected": false,
    "purpose_id": 23
  },
  {
    "name": "User Management",
    "description": "Designed for effective management of user roles and access rights.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 23,
    "selected": false,
    "purpose_id": 24
  },
  {
    "name": "Exchange Online Administration",
    "description": "Intended for administering and managing Exchange Online services.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 23,
    "selected": false,
    "purpose_id": 25
  },
  {
    "name": "SharePoint Online Administration",
    "description": "Geared towards effectively running SharePoint Online services.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 23,
    "selected": false,
    "purpose_id": 26
  },
  {
    "name": "Microsoft Teams Administration",
    "description": "Custom-built for managing and organizing Microsoft Teams services.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 23,
    "selected": false,
    "purpose_id": 27
  },
  {
    "name": "License Management",
    "description": "Created for the efficient handling of software licenses within the organization.",
    "transformations": "[\"REMOVEBG\"]",
    "parent_id": 23,
    "selected": false,
    "purpose_id": 28
  }
]
export default mockTreeData;