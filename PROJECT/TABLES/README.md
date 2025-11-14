<h1>🏥 Healthcare Data Warehouse – ERD Overview</h1>

<h2>📌 dim_patient (Patient Details)</h2>
<ul>
  <li><strong>Patient_ID (PK)</strong> – Unique patient ID</li>
  <li><strong>SSN</strong> – National identification number</li>
  <li><strong>PREFIX / FIRST / LAST / SUFFIX / MAIDEN</strong> – Name components</li>
  <li><strong>MARITAL</strong> – Marital status</li>
  <li><strong>GENDER</strong> – Patient gender</li>
  <li><strong>BIRTHDATE / DEATHDATE</strong> – Birth and death dates</li>
</ul>

<hr>

<h2>📌 dim_location (Location Information)</h2>
<ul>
  <li><strong>Location_Key (PK)</strong> – Unique location ID</li>
  <li><strong>ADDRESS, CITY, STATE, COUNTY, ZIP</strong> – Full address details</li>
  <li><strong>LAT, LON</strong> – Geographic coordinates</li>
</ul>

<hr>

<h2>📌 dim_date (Date Breakdown)</h2>
<ul>
  <li><strong>Date_Key (PK)</strong> – Surrogate key for date</li>
  <li><strong>Full_Date</strong> – Actual date</li>
  <li><strong>Year, Month, Quarter</strong> – Calendar components</li>
</ul>

<hr>

<h2>📌 dim_demographics (Demographic Attributes)</h2>
<ul>
  <li><strong>Demographic_Key (PK)</strong> – Unique demographic ID</li>
  <li><strong>RACE, ETHNICITY</strong> – Demographic classifications</li>
  <li><strong>BIRTHPLACE</strong> – Place of birth</li>
</ul>

<hr>

<h2>📌 fact_patient_health (Healthcare Measures)</h2>
<ul>
  <li><strong>Patient_ID, Date_Key, Location_Key</strong> – Foreign keys linking to dimensions</li>
  <li><strong>Healthcare_Expenses</strong> – Cost of healthcare services</li>
  <li><strong>Healthcare_Coverage</strong> – Insurance or coverage details</li>
</ul>

<hr>

<h2>⭐ Summary</h2>
<p>
This schema follows a <strong>star model</strong> where the fact table stores measurable healthcare events, and 
the dimension tables provide context about patients, demographics, dates, and locations. This structure 
enables accurate, historical, and flexible healthcare analytics.
</p>

