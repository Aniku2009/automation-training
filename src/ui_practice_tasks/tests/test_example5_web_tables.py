"""
Task 05 — Web Tables
URL: https://demoqa.com/webtables
"""

import pytest


# @pytest.mark.parametrize(
#     "base_url",
#     #["use_table_url"],
#     ["use_base_url"],
#     indirect=True
# )
def test_web_tables_add_new_user_row_appears(web_tables_page):
        #test_page_web_tables = web_tables_page("use_base_url")
        test_page_web_tables = web_tables_page("use_table_url")

        first_name = "Alice"
        last_name = "Cooper"
        email = "alice.cooper@example.com"
        age = "28"
        salary = "45000"
        department = "QA"

        test_page_web_tables.click_add_registration_form_button()
        test_page_web_tables.fill_reg_form(
                first_name=first_name,
                last_name=last_name,
                email=email,
                age=age,
                salary=salary,
                department=department,
        )
        test_page_web_tables.click_submit_button()

        assert test_page_web_tables.is_registration_form_hidden()
        assert test_page_web_tables.has_email_in_table(email)
        assert test_page_web_tables.has_first_name_in_table(first_name)
