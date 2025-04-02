**Problem: Comment Thread Optimization**

**Introduction:**

You are tasked with optimizing the display of comment threads for a high-volume platform. User comments can be nested to any depth, creating complex discussions. To enhance user engagement and minimize server load, you need to select a subset of comments for display that maximizes the total user engagement score while adhering to a depth constraint.

**Problem Description:**

Each comment in a thread has a unique `id`, a `score` (representing user engagement, e.g., likes minus dislikes), and a list of `children` comments (nested comments). Your goal is to write a function that selects the optimal subset of comments to display, maximizing the sum of their scores, while respecting the maximum allowed comment depth.

**Constraints:**

1.  **Depth Limit (D):** The *selection process* must ensure that no comment at a depth exceeding `D` is included in the output.
2.  **Parent-Child Dependency:** If a child comment is included in the displayed subset, its parent comment must also be included.
3.  **Order Preservation:** The displayed comments must maintain their original order within the thread.

**Input:**

Your function should take the following inputs:

* `thread`: A nested data structure representing the comment thread. Each comment is represented as a dictionary with the following structure:

    ```python
    {
        "id": <integer>,
        "score": <integer>,
        "text": <string>,
        "children": [<list of child comment dictionaries>]
    }
    ```

* `depth_limit`: An integer representing the maximum *allowed depth* of comments in the *selected subset*.

**Output:**

Your function should return a list of comment `id`s representing the optimal subset of comments to display, maximizing the total score while *adhering to the depth limit during selection*, and respecting all other constraints.

**Example:**

**Input:**

```python
thread = {
    "id": 1, "score": 10, "children": [
        {"id": 2, "score": 5, "children": [
            {"id": 4, "score": -2, "children": []},
            {"id": 5, "score": 8, "children": []}
        ]},
        {"id": 3, "score": -3, "children": [
            {"id": 6, "score": 7, "children": []}
        ]}
    ]
}

depth_limit = 2
```

**Expected Output:**

```python
[1, 2, 5, 3, 6] # or [1,2,5] or [1,2,4,5] or [1,3,6]
```

* Note: There might be multiple optimal solutions. The solution provided must be one of the optimal solutions.
* Note: The sum of the scores of the returned ids, must be the maximum sum possible under the given constraints.

**Constraints Summary:**

* Maximum thread depth: 10
* Maximum number of comments in a thread: 1000
* Comment scores: -100 to 100

**Evaluation Criteria:**

* **Correctness:** The solution should produce the optimal set of comment `id`s.
* **Efficiency:** The solution should avoid redundant calculations and have reasonable time and space complexity.
* **Code Quality:** The code should be clean, readable, and well-structured.
* **Explanation:** The candidate should be able to explain their approach and reasoning.
* **Edge Cases:** The solution should handle edge cases gracefully.

**Instructions:**

1.  Please write your solution in Python.
2.  Provide clear and concise comments to explain your code.
3.  Please submit your solution as a public git repository URL. (You can reply the email coming with this file the URL to your repository).
4.  We provide the example to comments data in the `comments.json` file coming with this problem statement file.

**Thank you & Good luck!**