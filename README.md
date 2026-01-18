### 🎢 Europa‑Park Coaster Recommender Test case

This is the automated test case of the coaster recommender.
The following 4 types of categories were tested:

Test Categories
1. Flow Tests (Scenario-Based Tests)
These tests verify the full user flow of the recommender system.
They simulate realistic user actions, such as submitting a height, triggering validation, and receiving the correct recommendation page.
They ensure that the application behaves correctly from the user’s perspective.

2. Validation Tests (Error Handling)
These tests check how the application responds to invalid or missing input.
They confirm that unrealistic values, empty fields, or out‑of‑range heights produce the correct error messages without crashing the system.
This ensures robustness and safe handling of user input.

3. Logic Tests (Parameterized Recommendation Paths)
These tests focus on the internal decision logic of the recommender.
By parameterizing multiple height values, they verify that each height leads to the correct recommendation category.
This provides efficient coverage of the core logic without repeating code.

4. Coaster Page Tests (Content & Routing)
These tests ensure that every coaster page defined in the application loads successfully.
They also verify that unknown coaster names correctly return a 404 error.
This protects against broken links and ensures data consistency.
