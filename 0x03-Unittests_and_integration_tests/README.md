# 📦 0x03. Unittests and Integration Tests

Welcome to the **Unittests and Integration Tests** project - part of the ALX Backend curriculum. In this project, you'll learn how to write effective Python tests using unit testing, integration testing, mocking, parameterization, and fixtures.

---

### 📂 Project Structure

alx-backend-python/
└── 0x03-Unittests_and_integration_tests/
├── client.py
├── fixtures.py
├── test_client.py
├── test_utils.py
├── utils.py
└── README.md

## 🧠 Learning Objectives

By the end of this project, you should be able to:

- Distinguish between **unit** and **integration** tests
- Use common patterns like **mocking**, **parameterization**, and **fixtures**
- Understand **memoization** and how to test it
- Apply testing to REST APIs using **mocked HTTP requests**

---

## 🛠️ Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- `pycodestyle` 2.5
- All files must:
  - End with a new line
  - Be executable
  - Have full module, class, and function docstrings
  - Include type annotations
- Tests should be run using:

```bash
python3 -m unittest path/to/test_file.py
```

## ✅ Tasks Overview

### 0. Parameterize a Unit Test

- Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.
- Test `utils.access_nested_map` using `@parameterized.expand`.
- Use the following inputs:
  - `nested_map={"a": 1}, path=("a",)`
  - `nested_map={"a": {"b": 2}}, path=("a",)`
  - `nested_map={"a": {"b": 2}}, path=("a", "b")`
- Use `assertEqual` to check for expected outputs.

---

### 1. Parameterize for Exceptions

- Implement `TestAccessNestedMap.test_access_nested_map_exception`.
- Use `@parameterized.expand` and `assertRaises` to check for `KeyError` with:
  - `nested_map={}, path=("a",)`
  - `nested_map={"a": 1}, path=("a", "b")`
- Validate that the exception message is correct.

---

### 2. Mock HTTP Calls

- Implement `TestGetJson` to test `utils.get_json`.
- Use `unittest.mock.patch` to patch `requests.get`.
- Provide a mock `json()` method that returns test payloads.
- Test with:
  - `test_url="http://example.com", test_payload={"payload": True}`
  - `test_url="http://holberton.io", test_payload={"payload": False}`
- Ensure `requests.get` is called once per input and output matches `test_payload`.

---

### 3. Memoization Test

- Implement `TestMemoize` class and `test_memoize` method.
- Create a class `TestClass` with:

  ```python
  def a_method(self):
      return 42

  @memoize
  def a_property(self):
      return self.a_method()
  ```

### 4. Patch as Decorators

- Create the `TestGithubOrgClient` class in `test_client.py`.
- Implement the `test_org` method to test `GithubOrgClient.org`.
- Use `@patch('client.get_json')` as a decorator to patch `get_json`.
- Use `@parameterized.expand` to test with:
  - `"google"`
  - `"abc"`
- Ensure that:
  - `get_json` is called once with the correct argument.
  - The actual function is not executed.

---

### 5. Mocking a Property

- Implement the `test_public_repos_url` method.
- Test the `_public_repos_url` property of `GithubOrgClient`.
- Use `patch` as a context manager to mock `GithubOrgClient.org`.
- Return a known payload (e.g. `{"repos_url": "https://api.github.com/orgs/test/repos"}`).
- Assert that `_public_repos_url` returns the expected URL.

---

### 6. More Patching

- Implement `test_public_repos` in `TestGithubOrgClient`.
- Use `@patch('client.get_json')` to mock `get_json`.
- Use `patch` as a context manager to mock `_public_repos_url`.
- Define expected payload and expected result.
- Assert that:
  - `public_repos` returns the correct list of repo names.
  - `_public_repos_url` is called once.
  - `get_json` is called once.

---

### 7. Parameterize License Checker

- Implement `test_has_license` to test `GithubOrgClient.has_license`.
- Use `@parameterized.expand` to test with:
  - `repo={"license": {"key": "my_license"}}, license_key="my_license"` → `True`
  - `repo={"license": {"key": "other_license"}}, license_key="my_license"` → `False`
- Assert that the returned result matches the expected boolean.

---

### 8. Integration Test Fixtures

- Create a new class: `TestIntegrationGithubOrgClient(unittest.TestCase)`
- Use `@parameterized_class` to provide fixtures:
  - `org_payload`
  - `repos_payload`
  - `expected_repos`
  - `apache2_repos`
- In `setUpClass`:

  - Patch `requests.get()` to return different mocked `.json()` responses using `side_effect`.
  - Start the patcher and assign it to `cls.get_patcher`.

- In `tearDownClass`:
  - Stop the patcher.

---

### 9. Integration Tests

- In `TestIntegrationGithubOrgClient`, implement:

#### `test_public_repos`

- Call `public_repos()` with no arguments.
- Assert that the result matches the `expected_repos` from fixtures.

#### `test_public_repos_with_license`

- Call `public_repos(license="apache-2.0")`.
- Assert that the result matches the `apache2_repos` from fixtures.

---

### 🧪 Running Tests

Run individual test files using:

```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
```
