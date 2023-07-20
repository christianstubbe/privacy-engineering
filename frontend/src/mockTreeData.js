const mockTreeData = [
  {
    "purpose_id": 1,
    "name": "Marketing",
    "selected": false,
    "transformations": [
      "BLUR",
      "REMOVEBG"
    ],
    "parent_id": null,
    "children": [
      {
        "purpose_id": 2,
        "name": "Offline",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 1,
        "children": [
          {
            "purpose_id": 3,
            "name": "Print Advertising",
            "selected": false,
            "transformations": [
              "REMOVEBG"
            ],
            "parent_id": 2,
            "children": []
          },
          {
            "purpose_id": 4,
            "name": "Outdoor Advertising",
            "selected": false,
            "transformations": [
              "REMOVEBG"
            ],
            "parent_id": 2,
            "children": []
          },
          {
            "purpose_id": 5,
            "name": "Event Marketing",
            "selected": false,
            "transformations": [
              "REMOVEBG"
            ],
            "parent_id": 2,
            "children": []
          },
          {
            "purpose_id": 6,
            "name": "TV and Radio Advertising",
            "selected": false,
            "transformations": [
              "REMOVEBG"
            ],
            "parent_id": 2,
            "children": []
          }
        ]
      },
      {
        "purpose_id": 7,
        "name": "Online",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 1,
        "children": [
          {
            "purpose_id": 8,
            "name": "Social Media",
            "selected": false,
            "transformations": [
              "BLACKWHITE"
            ],
            "parent_id": 7,
            "children": [
              {
                "purpose_id": 9,
                "name": "LinkedIn",
                "selected": false,
                "transformations": [
                  "BLACKWHITE"
                ],
                "parent_id": 8,
                "children": []
              },
              {
                "purpose_id": 10,
                "name": "Instagram",
                "selected": false,
                "transformations": [
                  "BLACKWHITE"
                ],
                "parent_id": 8,
                "children": []
              },
              {
                "purpose_id": 11,
                "name": "Facebook",
                "selected": false,
                "transformations": [
                  "BLACKWHITE"
                ],
                "parent_id": 8,
                "children": []
              }
            ]
          },
          {
            "purpose_id": 12,
            "name": "Website",
            "selected": false,
            "transformations": [
              "BLACKWHITE"
            ],
            "parent_id": 7,
            "children": []
          }
        ]
      }
    ]
  },
  {
    "purpose_id": 13,
    "name": "HR",
    "selected": false,
    "transformations": [],
    "parent_id": null,
    "children": [
      {
        "purpose_id": 14,
        "name": "Recruitment",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 13,
        "children": []
      },
      {
        "purpose_id": 15,
        "name": "Payroll Processing",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 13,
        "children": []
      },
      {
        "purpose_id": 16,
        "name": "Training and Development",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 13,
        "children": []
      },
      {
        "purpose_id": 17,
        "name": "Performance Evaluation",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 13,
        "children": []
      }
    ]
  },
  {
    "purpose_id": 18,
    "name": "Sales",
    "selected": false,
    "transformations": [
      "BLACKWHITE"
    ],
    "parent_id": null,
    "children": [
      {
        "purpose_id": 19,
        "name": "Customer Relationship Management Access",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 18,
        "children": []
      },
      {
        "purpose_id": 20,
        "name": "Sales Order Processing",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 18,
        "children": []
      },
      {
        "purpose_id": 21,
        "name": "Sales Campaign Management",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 18,
        "children": []
      },
      {
        "purpose_id": 22,
        "name": "Sales Forecasting",
        "selected": false,
        "transformations": [
          "BLACKWHITE"
        ],
        "parent_id": 18,
        "children": []
      }
    ]
  },
  {
    "purpose_id": 23,
    "name": "Microsoft 365",
    "selected": false,
    "transformations": [
      "REMOVEBG"
    ],
    "parent_id": null,
    "children": [
      {
        "purpose_id": 24,
        "name": "User Management",
        "selected": false,
        "transformations": [
          "REMOVEBG"
        ],
        "parent_id": 23,
        "children": []
      },
      {
        "purpose_id": 25,
        "name": "Exchange Online Administration",
        "selected": false,
        "transformations": [
          "REMOVEBG"
        ],
        "parent_id": 23,
        "children": []
      },
      {
        "purpose_id": 26,
        "name": "SharePoint Online Administration",
        "selected": false,
        "transformations": [
          "REMOVEBG"
        ],
        "parent_id": 23,
        "children": []
      },
      {
        "purpose_id": 27,
        "name": "Microsoft Teams Administration",
        "selected": false,
        "transformations": [
          "REMOVEBG"
        ],
        "parent_id": 23,
        "children": []
      },
      {
        "purpose_id": 28,
        "name": "License Management",
        "selected": false,
        "transformations": [
          "REMOVEBG"
        ],
        "parent_id": 23,
        "children": []
      }
    ]
  }
];

export default mockTreeData;