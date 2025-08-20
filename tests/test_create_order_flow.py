import random
from playwright.sync_api import expect

from ui.pages.login_page import LoginPage
from ui.pages.order_page import OrderPage

def test_create_order_with_sample_and_test(page, base_url, creds):
    # 1) Authentication
    login = LoginPage(page)
    login.goto(base_url)
    login.login(creds["email"], creds["password"])
    expect(login.welcome_message).to_be_visible(timeout=10_000)

    # 2) Order Creation
    order = OrderPage(page)
    order.start_new_order()
    order.details.choose_customer("— ACME Labs")
    order.details.choose_user("QA Engineer")
    order.details.save()
    expect(order.details.status_created).to_be_visible(timeout=10_000)

    # 3) Sample Creation
    order.samples.create_one_sample()
    order.samples.fill_sample_fields(
        lab_id=str(random.randint(1, 9999)),
        sample_type="dummy",
        description="description",
        day="20",
        point="point",
    )
    order.samples.save()
    expect(order.samples.created_sample_row_link).to_be_visible(timeout=10_000)

    # 4) Test Addition
    order.tests.add_test(assay_name="- Amino Acids", assignee="QA Engineer")
    expect(order.tests.test_id).to_be_visible(timeout=10_000)
    order.toast.expect_text("Tests successfully saved!")
