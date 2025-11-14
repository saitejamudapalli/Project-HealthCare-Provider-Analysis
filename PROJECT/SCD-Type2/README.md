<h1>🩺 SCD Type-2 — Summary & Explanation</h1>

<h2>✅ What is SCD Type-2?</h2>
<p>
  SCD Type-2 (Slowly Changing Dimension Type 2) is a data-warehousing technique used to 
  <strong>track historical changes</strong> in dimension tables.
</p>
<p>
  Instead of overwriting existing patient information when something changes, SCD-2:
</p>
<ul>
  <li>Closes the old record (<code>end_date</code>, <code>is_current_flag = FALSE</code>)</li>
  <li>Inserts a new version of the record (<code>start_date = current_date</code>, <code>is_current_flag = TRUE</code>)</li>
</ul>

<p>This helps answer important questions such as:</p>
<ul>
  <li>“What was the patient’s name last year?”</li>
  <li>“What gender was recorded during the patient’s 2021 visit?”</li>
  <li>“How has this patient’s demographic information changed over time?”</li>
</ul>

<br>

<h2>🎯 Why SCD Type-2 Is Needed in This Healthcare Project</h2>
<p>Patient information in healthcare changes frequently, including:</p>
<ul>
  <li>Name corrections (marriage, spelling fix)</li>
  <li>Gender updates</li>
  <li>Demographic modifications</li>
</ul>

<p>
  Analytics require <strong>historical accuracy</strong>. If we overwrite old values, 
  all past reports will incorrectly show the new updated data.
</p>

<p><strong>Example Issue Without SCD-2:</strong></p>
<p>
  If a patient's gender changes today, all historical reports will also show the updated gender,
  which is incorrect.
</p>

<p>SCD-2 prevents this by:</p>
<ul>
  <li>Keeping old versions (historical records)</li>
  <li>Creating a new version for every change</li>
  <li>Marking only one row as <code>is_current_flag = TRUE</code></li>
</ul>

<br>

<h2>🔍 Why This Logic Is Useful</h2>

<h3>✔ Full Historical Tracking</h3>
<p>See exactly when and how each patient detail changed.</p>

<h3>✔ Accurate Reporting</h3>
<p>Past analysis reflects the correct values used at that time.</p>

<h3>✔ Audit & Compliance Ready</h3>
<ul>
  <li>Clear audit trail</li>
  <li>Traceable record history</li>
  <li>Regulatory-friendly data lineage</li>
</ul>

<h3>✔ Better Analytics</h3>
<ul>
  <li>Demographic trend analysis</li>
  <li>Understanding patient data evolution</li>
  <li>Impact of corrections on medical outcomes</li>
</ul>

<br>

<h2>💡 Final Summary</h2>
<p>
  Your SCD Type-2 pipeline ensures patient information changes are historically tracked by closing old records 
  and inserting new ones, enabling complete historical visibility and accurate healthcare analytics.
</p>
