<h1 align="center">🏥 Healthcare Provider Analysis Dashboard</h1>

<p align="center">
An interactive <b>Streamlit-based data analysis dashboard</b> designed to explore and visualize healthcare provider and patient data.  
This project provides deep insights into <b>demographics</b>, <b>financial trends</b>, and <b>geographical distributions</b> — empowering analysts and healthcare professionals to make data-driven decisions.
</p>

---

<h2>📘 Table of Contents</h2>

<ul>
  <li><a href="#overview">🩺 Overview</a></li>
  <li><a href="#architecture">🧱 Architecture</a></li>
  <li><a href="#features">✨ Dashboard Features</a></li>
  <li><a href="#data-source">📈 Data Source</a></li>
  <li><a href="#stack">🛠 Technology Stack</a></li>
  <li><a href="#structure">📂 Project Structure</a></li>
  <li><a href="#setup">⚙️ Setup and Deployment</a></li>
  <li><a href="#sections">🧭 Dashboard Sections</a></li>
  <li><a href="#enhancements">🚀 Future Enhancements</a></li>
  <li><a href="#author">👤 Author</a></li>
  <li><a href="#preview">📸 Dashboard Preview</a></li>
</ul>

---

<h2 id="overview">🩺 Overview</h2>

<p>
The <b>Healthcare Provider Analysis Dashboard</b> delivers an end-to-end visualization and data analysis solution that enables users to:
</p>

<ul>
  <li>📊 Explore demographic trends</li>
  <li>💰 Analyze healthcare expenses and coverage</li>
  <li>🌍 Understand geographic distribution</li>
  <li>🔍 Identify correlations across multiple health indicators</li>
</ul>

<p>
This project transforms cleaned and structured healthcare data into actionable insights through an intuitive and interactive interface.
</p>

---

<h2 id="architecture">🧱 Architecture</h2>

<pre>
+------------------+       +---------------------+       +------------------------+       +--------------------------+
|   Raw Data       | --->  |   Data Cleaning     | --->  |   Processed (Silver)   | --->  |   Streamlit Dashboard     |
|  (CSV / Source)  |       | (Nulls, Type Fixes) |       |   Dataset (CSV)        |       |   (Interactive UI)        |
+------------------+       +---------------------+       +------------------------+       +--------------------------+
</pre>

<ul>
  <li><b>Raw Layer:</b> Original patient dataset from multiple sources.</li>
  <li><b>Silver Layer:</b> Cleaned, standardized dataset (<code>PATIENTS_SILVER.csv</code>).</li>
  <li><b>Dashboard Layer:</b> Visual analytics built with Streamlit and Plotly.</li>
</ul>

---

<h2 id="features">✨ Dashboard Features</h2>

<ul>
  <li>🎨 <b>Modern Streamlit Interface</b> – clean, intuitive, and responsive UI.</li>
  <li>👩‍⚕️ <b>Demographics Insights</b> – analyze gender, race, age, and marital status patterns.</li>
  <li>💰 <b>Financial Overview</b> – track expenses, coverage, and patient spending behavior.</li>
  <li>🌍 <b>Geographic Visualization</b> – interactive location-based mapping of patients.</li>
  <li>🔥 <b>Correlation Analysis</b> – visualize relationships among key health metrics.</li>
  <li>⚡ <b>Optimized Performance</b> with caching and real-time rendering.</li>
</ul>

---

<h2 id="data-source">📈 Data Source</h2>

<table>
  <tr><td><b>Dataset Name:</b></td><td>PATIENTS_SILVER.csv</td></tr>
  <tr><td><b>Type:</b></td><td>Structured CSV file</td></tr>
</table>

<p><b>Data Includes:</b></p>
<ul>
  <li>Patient demographic details</li>
  <li>Financial data (expenses, coverage)</li>
  <li>Geographic information (city, state, coordinates)</li>
</ul>

<p><b>Cleaning Steps:</b></p>
<ul>
  <li>Removed null or inconsistent entries</li>
  <li>Converted date and numeric fields</li>
  <li>Standardized column names and formats</li>
</ul>

---

<h2 id="stack">🛠 Technology Stack</h2>

<table>
  <tr><th>Category</th><th>Tools / Libraries</th></tr>
  <tr><td><b>Programming Language</b></td><td>Python</td></tr>
  <tr><td><b>Framework</b></td><td>Streamlit</td></tr>
  <tr><td><b>Data Handling</b></td><td>Pandas, NumPy</td></tr>
  <tr><td><b>Visualization</b></td><td>Plotly Express</td></tr>
  <tr><td><b>Version Control</b></td><td>Git, GitHub</td></tr>
  <tr><td><b>Presentation</b></td><td>Microsoft PowerPoint (.pptx)</td></tr>
</table>

---

<h2 id="structure">📂 Project Structure</h2>

<pre>
Project-HealthCare-Provider-Analysis/
│
├── app/
│   ├── Home.py
│   ├── Demographics.py
│   ├── Financial.py
│   ├── Geographic.py
│   └── DataExplorer.py
│
├── data/
│   └── PATIENTS_SILVER.csv
│
├── docs/
│   └── Healthcare_Critical_Analysis_Presentation.pptx
│
├── requirements.txt
└── README.md
</pre>

<p><b>Folder Descriptions:</b></p>
<ul>
  <li>🧩 <b>app/</b> → Streamlit page scripts (modular dashboard components)</li>
  <li>📊 <b>data/</b> → Cleaned Silver Layer dataset</li>
  <li>🧾 <b>docs/</b> → Presentation and project documentation</li>
  <li>⚙️ <b>requirements.txt</b> → Python dependencies</li>
</ul>

---

<h2 id="setup">⚙️ Setup and Deployment</h2>

<h3>🪜 Steps to Run Locally</h3>

<ol>
  <li><b>Clone the Repository:</b>
    <pre><code>git clone https://github.com/saitejamudapalli/Project-HealthCare-Provider-Analysis.git
cd Project-HealthCare-Provider-Analysis</code></pre>
  </li>

  <li><b>Install Dependencies:</b>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><b>Run the Dashboard:</b>
    <pre><code>streamlit run Home.py</code></pre>
  </li>

  <li><b>Open in Browser:</b>
    <pre><code>http://localhost:8501</code></pre>
  </li>
</ol>

---

<h2 id="sections">🧭 Dashboard Sections</h2>

<h3>🏠 Home (Key Metrics)</h3>
<ul>
  <li>👥 Total Patients</li>
  <li>👨‍⚕️ Male vs Female Ratio</li>
  <li>💸 Average Healthcare Expenses</li>
  <li>💳 Average Healthcare Coverage</li>
</ul>

<h3>👩‍⚕️ Demographics</h3>
<ul>
  <li>🧍 Gender Distribution (Pie Chart)</li>
  <li>🌈 Race Diversity (Bar Chart)</li>
  <li>💍 Marital Status (Bar Chart)</li>
  <li>🎂 Age Distribution (Histogram)</li>
</ul>

<h3>💰 Financial Insights</h3>
<ul>
  <li>📊 Expense Distribution (Histogram)</li>
  <li>🔗 Coverage vs Expenses (Scatter Plot)</li>
  <li>🧾 Average Expenses by Gender (Bar Chart)</li>
</ul>

<h3>🌍 Geographic Distribution</h3>
<ul>
  <li>🗺️ City and State-wise Patient Distribution</li>
  <li>💵 Expense and Coverage Visualization across Regions</li>
</ul>

<h3>🧮 Data Explorer</h3>
<ul>
  <li>🔥 Correlation Heatmap of numerical columns</li>
  <li>📈 Identify relationships between key metrics</li>
</ul>

---

<h2 id="enhancements">🚀 Future Enhancements</h2>

<ul>
  <li>🔄 Real-time data integration via APIs</li>
  <li>🤖 Predictive analytics for healthcare outcomes</li>
  <li>🧠 Machine learning-based forecasting</li>
  <li>☁️ Cloud deployment (Streamlit Cloud / AWS)</li>
</ul>

---

<h2 id="author">👤 Author</h2>

<p>
👨‍💻 <b>Saiteja Mudapalli</b><br>
📧 <i>mudapallisaiteja@gmail.com</i><br>
🔗 <a href="https://github.com/saitejamudapalli" target="_blank">GitHub Profile</a>
</p>

---

<h2 id="preview">📸 Dashboard Preview</h2>

<table>
  <tr><th>Section</th><th>Preview</th></tr>
  <tr><td>🏠 Home – Key Metrics</td><td><i><img width="1758" height="628" alt="home" src="https://github.com/user-attachments/assets/1b84b11e-c4c8-4e18-8306-793131f6b51c" />
</i></td></tr>
  <tr><td>👩‍⚕️ Demographics Overview</td><td><i><img width="1763" height="659" alt="Screenshot 2025-11-13 205831" src="https://github.com/user-attachments/assets/4c8bc9fc-e277-4866-834c-eba9d8051545" />
<img width="1796" height="627" alt="Screenshot 2025-11-13 210005" src="https://github.com/user-attachments/assets/03976234-fb2c-4cf9-95df-02626a3b49e2" />
<img width="1806" height="538" alt="Screenshot 2025-11-13 210023" src="https://github.com/user-attachments/assets/e693cce4-753e-41d3-8b20-3110cc265e24" />
<img width="1760" height="637" alt="Screenshot 2025-11-13 210054" src="https://github.com/user-attachments/assets/be87cb44-1272-4cd8-9f71-b7a25f999526" />)</i></td></tr>
  <tr><td>💰 Financial Insights</td><td><i><img width="1764" height="659" alt="Screenshot 2025-11-13 210555" src="https://github.com/user-attachments/assets/9e1e3a0d-8dc5-4b21-b6ed-6d1dfb8e8371" />
<img width="1757" height="586" alt="Screenshot 2025-11-13 210617" src="https://github.com/user-attachments/assets/6efa00d9-9de2-41d6-8510-ca715f74084f" />
<img width="1767" height="592" alt="Screenshot 2025-11-13 210635" src="https://github.com/user-attachments/assets/0c1747e0-63d0-46e8-97d1-364a47896b43" />
</i></td></tr>
  <tr><td>🌍 Geographic Distribution</td><td><i><img width="1759" height="623" alt="Screenshot 2025-11-13 211037" src="https://github.com/user-attachments/assets/bdcd3614-a7be-458b-9e45-0832c41b699a" />
</i></td></tr>
  <tr><td>🧮 Data Explorer (Heatmap)</td><td><i><img width="1745" height="835" alt="Screenshot 2025-11-13 211119" src="https://github.com/user-attachments/assets/255e4fdc-6ae5-4c40-a151-302e2411b8a8" />
</i></td></tr>
</table>

<p align="center">
🧭 Each section provides actionable insights into patient demographics, financial behavior, and healthcare accessibility.
</p>

---

<h3 align="center">💡 Developed with ❤️ by <b>Saiteja Mudapalli</b></h3>
