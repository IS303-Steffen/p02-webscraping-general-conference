### MAX SCORE: 100
### YOUR SCORE:  
## Grader's Notes:
- TAs: Put any notes on points lost here.

---

## Rubric

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>#</th>
      <th>Requirement</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Includes repeating menu</td>
      <td>3</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Starts off on the general conference page that lists all the talks in the session</td>
      <td>5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Loads all the pages for the talks, but leaves out the non-talk pages specified in the instructions</td>
      <td>15</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Successfully scrapes the speaker name, talk name, kicker, and number of references to books of scripture into Python for all talks with references</td>
      <td>20</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Successfully scrapes data from talks that don't have references</td>
      <td>20</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Successfully exports the data to Excel using pandas</td>
      <td>10</td>
    </tr>
    <tr>
      <td>7</td>
      <td>For option 2, successfully handles a missing file</td>
      <td>1</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Displays summary data of the top 10 referenced books of scripture</td>
      <td>10</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Displays summary data of talks that referenced Doctrine and Covenants the most</td>
      <td>15</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Includes comments</td>
      <td>1</td>
    </tr>
    <tr>
      <td colspan="2">Total</td>
      <td>100</td>
    </tr>
  </tbody>
</table>

---

## TA Guide (Partial Credit Suggestions)

1. #### Includes repeating menu — 3 pts
   - Full credit: Menu loops until “Exit” is entered; invalid inputs handled gracefully.
   - -1 if menu does not repeat (runs once then exits).
   - -1 if “Exit”/exit path not handled (can’t quit cleanly).
   - -1 if invalid options cause a crash or no feedback.

2. #### Starts off on the general conference page that lists all the talks in the session — 5 pts
   - Full credit: Navigates to the correct session landing page.
   - -3 wrong session or wrong base URL.
   - -2 heavy hardcoding that wouldn’t generalize to another session (e.g., clicking by brittle absolute indices).

3. #### Loads all the pages for the talks, leaving out non-talk pages — 15 pts
   - Full credit: Visits each talk page; excludes session/video pages and “Sustaining…” page.
   - -8 includes non-talk pages (session/sustaining) or crashes on them.
   - -4 only partial coverage (misses several talks due to selector logic).
   - -3 fails to handle relative links (e.g., forgets to prepend base URL).

4. #### Scrapes speaker, talk title, kicker, and reference counts (talks with references) — 20 pts
   - Full credit: All three metadata fields + accurate counts for books (using the related content panel).
   - -5 missing any of the three fields (speaker/title/kicker).
   - -6 incorrect counts (never opens “Related Content” or reads the wrong element).
   - -2 doesn’t normalize non-breaking spaces when using `.text_content()` (counts silently wrong).
   - -5 only scrapes a subset of talks with references.

5. #### Scrapes data from talks that don’t have references — 20 pts
   - Full credit: Handles missing related content panel without crashing; still captures speaker/title/kicker.
   - -10 crashes or skips talk entirely on missing references.
   - -6 collects metadata but leaves reference counts in an inconsistent state (e.g., None vs 0).
   - -4 works for some no-reference talks but not others.

6. #### Exports data to Excel using pandas — 10 pts
   - Full credit: DataFrame created and exported to `conference_talks_data.xlsx`; columns align with dictionary keys; `index=False`.
   - -3 unreadable file (missing extension/format issues).
   - -1 includes stray index column or missing expected columns.
   - -2 exports in a different format than specified (CSV) without justification.

7. #### Option 2 gracefully handles a missing file — 1 pt
   - Full credit: Catches missing file and returns to menu with a clear message.
   - -1 crashes on `FileNotFoundError` or hangs.

8. #### Displays top 10 referenced books of scripture — 10 pts
   - Full credit: Aggregates across all talks; sorts descending; shows top 10 books only.
   - -5 incorrect set (not top 10 / unsorted / includes non-book columns).
   - -3 off-by-one issues or shows more/less than 10 without rationale.
   - -2 unreadable output (e.g., unlabeled or mixed with debug noise).

9. #### Displays talks that referenced Doctrine and Covenants the most — 15 pts
   - Full credit: Finds max `Doctrine and Covenants` value; displays all talks tied for max with speaker, title, and count.
   - -5 shows only one talk when ties exist or doesn’t filter to max.
   - -2 missing columns (speaker/title) or mislabeled output.
   - -3 fragile query (breaks on column name with spaces or fails on zero-max case).

10. #### Includes comments — 1 pt
   - Full credit: Reasonable top-of-file header and inline comments explaining key steps.
   - -1 no meaningful comments (TA can still see intent but no explanation).