# 📊 PhonePe Pulse Data Visualization

A Streamlit web application that visualizes data extracted from the [PhonePe Pulse GitHub](https://github.com/PhonePe/pulse).

## 🔧 Features

- 📥 Cloned PhonePe Pulse data
- 🧠 Extracted and processed JSON data using Python
- 🗃️ Stored data into MySQL database
- 📈 Built an interactive Streamlit dashboard
- 🔍 Provides analysis like:
  - Top states and districts by transactions
  - Year-wise transaction trends
  - User and merchant activity heatmaps

## 💻 Tech Stack

- Python
- Streamlit
- MySQL
- Pandas
- Plotly
- SQLAlchemy

## 🚀 How to Run Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/YOUR-USERNAME/phonepe-project.git
    cd phonepe-project
    ```

2. Create virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## 📦 Folder Structure

phonepe_project/
│
├── .gitignore                    # Git ignore rules
├── README.md                     # Project overview
├── requirements.txt              # All dependencies listed
│
├── data/                         # Raw data (from PhonePe GitHub)
│   └── ...                       # JSON files (optional: ignore in Git)
│
├── database/                     # DB setup and insertion scripts
│   ├── connection.py             # Reusable DB connection
│   ├── create_database.py        # Create database + tables
│   └── insert_data.py            # Load JSON → Extract → Insert to SQL
│
├── queries/                      # SQL queries (reusable)
│   └── aggregated_insurance.sql
│
├── app/                          # Streamlit application
│   ├── __init__.py               # Makes this a Python package
│   ├── main.py                   # Streamlit entry point
│   │
│   ├── pages/                    # Multi-page layout for Streamlit
│   │   ├── 1_Aggregated_Transaction.py
│   │   ├── 2_Aggregated_Insurance.py
│   │   ├── 3_Map_User.py
│   │   ├── 4_Top_Insurance.py
│   │   └── ... (add more pages)
│   │
│   └── utils/                    # Helper functions and GeoJSON
│       ├── fetch_data.py         # SQL fetch logic
│       ├── chart_helpers.py      # Charts, plotting, map utils
│       └── state_geojson.json    # India map data for choropleth
│
└── india_map/                    # Optional: standalone map rendering
    └── india_choropleth.py
