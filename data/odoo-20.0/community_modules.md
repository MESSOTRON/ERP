# Odoo 20.0 Community – vollständige Modulliste

Automatisch erzeugt mit `scripts/odoo_module_inventory.py` aus dem offiziellen
Quellcode (github.com/odoo/odoo, Branch 20.0). Testmodule sind ausgelassen.

Typ: **App** = eigene Anwendung im Apps-Menü; **Erweiterung** = optional
installierbar; **Technisch/Brücke** = wird automatisch mitinstalliert, sobald
die abhängigen Apps installiert sind; **Lokalisierung** = Länderpaket.

## Accounting (44)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `account` | Invoicing | App | Accounting/Accounting | Invoices & Payments |
| `account_check_printing` | Check Printing Base | Erweiterung | Accounting/Accounting | Check printing basic features |
| `account_debit_note` | Debit Notes | Erweiterung | Accounting/Accounting | Debit Notes |
| `account_edi` | Import/Export Invoices From XML/PDF | Erweiterung | Accounting/Accounting |  |
| `account_edi_proxy_client` | Proxy features for account_edi | Erweiterung | Accounting/Accounting |  |
| `account_edi_ubl_cii` | Import/Export electronic invoices with UBL/CII | Technisch/Brücke | Accounting/Accounting |  |
| `account_fleet` | Accounting/Fleet bridge | Technisch/Brücke | Accounting/Accounting | Manage accounting with fleets |
| `account_payment` | Payment - Account | Technisch/Brücke | Accounting/Accounting | Enable customers to pay invoices on the portal and post payments when transactions are processed. |
| `account_payment_custom` | Payment Custom / Account Payment | Technisch/Brücke | Accounting/Payment Custom | Bridge between payment_custom and account_payment. |
| `account_payment_interco` | Intercompany Payment - Account | Erweiterung | Accounting/Accounting | Enable Intercompany payments to reconcile with their invoices on post. |
| `account_peppol` | Peppol | Technisch/Brücke | Accounting/Accounting | This module is used to send/receive documents with Peppol |
| `account_qr_code_emv` | account_qr_code_emv | Erweiterung | Accounting/Payment |  |
| `account_qr_code_sepa` | Account SEPA QR Code | Technisch/Brücke | Accounting/Payment |  |
| `account_tax_python` | Define Taxes as Python Code | Erweiterung | Accounting/Accounting | Use python code to define taxes |
| `account_test` | Accounting Consistency Tests | Erweiterung | Accounting/Accounting |  |
| `account_update_tax_tags` | Account - Allow updating tax grids | Erweiterung | Accounting/Accounting | Allow updating tax grids on existing entries |
| `analytic` | Analytic Accounting | Erweiterung | Accounting/Accounting |  |
| `payment_adyen` | Payment Provider: Adyen | Erweiterung | Accounting/Payment Providers | A Dutch payment provider covering Europe and the US. |
| `payment_aps` | Payment Provider: Amazon Payment Services | Erweiterung | Accounting/Payment Providers | An Amazon payment provider covering the MENA region. |
| `payment_asiapay` | Payment Provider: AsiaPay | Erweiterung | Accounting/Payment Providers | An payment provider based in Hong Kong covering most Asian countries. |
| `payment_authorize` | Payment Provider: Authorize.Net | Erweiterung | Accounting/Payment Providers | An payment provider covering the US, Australia, and Canada. |
| `payment_buckaroo` | Payment Provider: Buckaroo | Erweiterung | Accounting/Payment Providers | A Dutch payment provider covering several countries in Europe. |
| `payment_custom` | Payment Provider: Custom Payment Modes | Erweiterung | Accounting/Payment Providers | A payment provider for custom flows like wire transfers. |
| `payment_demo` | Payment Provider: Demo | Erweiterung | Accounting/Accounting | A payment provider for running fake payment flows for demo purposes. |
| `payment_dpo` | Payment Provider: DPO | Erweiterung | Accounting/Payment Providers | A Kenyan payment provider covering several African countries. |
| `payment_ecpay` | Payment Provider: ECPay | Erweiterung | Accounting/Payment Providers | A payment provider covering the Taiwanese market. |
| `payment_flutterwave` | Payment Provider: Flutterwave | Erweiterung | Accounting/Payment Providers | A Nigerian payment provider covering several African countries. |
| `payment_iyzico` | Payment Provider: Iyzico | Erweiterung | Accounting/Payment Providers | A payment provider covering Turkey. |
| `payment_mercado_pago` | Payment Provider: Mercado Pago | Erweiterung | Accounting/Payment Providers | A payment provider covering several countries in Latin America. |
| `payment_mollie` | Payment Provider: Mollie | Erweiterung | Accounting/Payment Providers | A Dutch payment provider covering several European countries. |
| `payment_nuvei` | Payment Provider: Nuvei | Erweiterung | Accounting/Payment Providers | A payment provider covering Latin America. |
| `payment_paymob` | Payment Provider: Paymob | Erweiterung | Accounting/Payment Providers | An Egyptian payment provider for the Middle East. |
| `payment_paypal` | Payment Provider: Paypal | Erweiterung | Accounting/Payment Providers | An American payment provider for online payments all over the world. |
| `payment_payu` | Payment Provider: PayU | Erweiterung | Accounting/Payment Providers | A payment provider covering India. |
| `payment_razorpay` | Payment Provider: Razorpay | Erweiterung | Accounting/Payment Providers | A payment provider covering India. |
| `payment_redsys` | Payment Provider: Redsys | Erweiterung | Accounting/Payment Providers | A payment provider covering the Spanish market. |
| `payment_stripe` | Payment Provider: Stripe | Erweiterung | Accounting/Payment Providers | An Irish-American payment provider covering the US and many others. |
| `payment_toss_payments` | Payment Provider: Toss Payments | Erweiterung | Accounting/Payment Providers | A payment provider covering the South Korea market |
| `payment_worldline` | Payment Provider: Worldline | Erweiterung | Accounting/Payment Providers | A French payment provider covering several European countries. |
| `payment_xendit` | Payment Provider: Xendit | Erweiterung | Accounting/Payment Providers | A payment provider for Indonesian and the Philippines. |
| `pos_account_tax_python` | Allow custom taxes in POS | Technisch/Brücke | Accounting/Accounting |  |
| `product_email_template` | Product Email Template | Erweiterung | Accounting/Accounting |  |
| `project_account` | Project - Account | Technisch/Brücke | Accounting/Accounting | project profitability items computation |
| `spreadsheet_account` | Spreadsheet Accounting Formulas | Technisch/Brücke | Accounting | Spreadsheet Accounting formulas |

## Administration (1)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `iot_webserial` | Web Serial IoT devices | Erweiterung | Administration/IoT | Interface with serial devices directly via the browser using Web Serial. |

## Extra Tools (3)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `auth_totp` | Two-Factor Authentication (TOTP) | Technisch/Brücke | Extra Tools |  |
| `auth_totp_mail` | 2FA Invite mail | Technisch/Brücke | Extra Tools |  |
| `rpc` | RPC endpoints | Technisch/Brücke | Extra Tools |  |

## Hidden (52)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `api_doc` | API Documentation | Technisch/Brücke | Hidden |  |
| `attachment_indexation` | Attachments List and Document Indexation | Technisch/Brücke | Hidden/Tools |  |
| `auth_ldap` | Authentication via LDAP | Technisch/Brücke | Hidden/Tools |  |
| `auth_oauth` | OAuth2 Authentication | Technisch/Brücke | Hidden/Tools |  |
| `auth_passkey` | Passkeys | Technisch/Brücke | Hidden/Tools | Log in with a Passkey |
| `auth_passkey_portal` | Passkeys Portal | Technisch/Brücke | Hidden/Tools | Passkeys for portal users |
| `auth_password_policy` | Password Policy | Technisch/Brücke | Hidden/Tools | Implement basic password policy configuration & check |
| `auth_password_policy_signup` | Password Policy support for Signup | Technisch/Brücke | Hidden/Tools |  |
| `auth_signup` | Signup | Technisch/Brücke | Hidden/Tools |  |
| `auth_timeout` | Auth Timeout | Technisch/Brücke | Hidden/Tools | Ask for authentication after user inactivity |
| `auth_totp_portal` | TOTPortal | Technisch/Brücke | Hidden |  |
| `base` | Base | Technisch/Brücke | Hidden |  |
| `base_import` | Base import | Technisch/Brücke | Hidden/Tools |  |
| `base_import_module` | Base import module | Technisch/Brücke | Hidden/Tools |  |
| `base_install_request` | Base - Module Install Request | Technisch/Brücke | Hidden |  |
| `base_report_paper_muncher` | Report Engine: Paper Muncher | Technisch/Brücke | Hidden/Tools | Paper Muncher Engine |
| `base_report_wkhtmltox` | Report Engine: wkhtmltopdf/wkhtmltoimage | Technisch/Brücke | Hidden/Tools | wkhtmltopdf rendering engine |
| `base_setup` | Initial Setup Tools | Technisch/Brücke | Hidden |  |
| `base_sparse_field` | Sparse Fields | Technisch/Brücke | Hidden | Implementation of sparse fields. |
| `bus` | IM Bus | Technisch/Brücke | Hidden |  |
| `certificate` | Certificate | Technisch/Brücke | Hidden/Tools | Manage certificate |
| `google_account` | Google Users | Technisch/Brücke | Hidden/Tools |  |
| `google_address_autocomplete` | Google Address Autocomplete | Technisch/Brücke | Hidden/Tools | Assist with automatic completion & suggestions when filling address |
| `google_gmail` | Google Gmail | Technisch/Brücke | Hidden |  |
| `google_recaptcha` | Google reCAPTCHA integration | Technisch/Brücke | Hidden |  |
| `hr_skills_event` | Skills Events | Technisch/Brücke | Hidden | Link training events to resume of your employees |
| `html_editor` | HTML Editor | Technisch/Brücke | Hidden | A Html Editor component and plugin system. |
| `http_routing` | Web Routing | Technisch/Brücke | Hidden | Web Routing |
| `iap` | In-App Purchase | Technisch/Brücke | Hidden/Tools | Basic models and helpers to support In-App Purchase. |
| `iap_crm` | IAP / CRM | Technisch/Brücke | Hidden/Tools | Bridge between IAP and CRM |
| `iap_mail` | IAP / Mail | Technisch/Brücke | Hidden/Tools | Bridge between IAP and mail |
| `iot_drivers` | Hardware Proxy | Technisch/Brücke | Hidden | Connect the Web Client to Hardware Peripherals |
| `microsoft_account` | Microsoft Users | Technisch/Brücke | Hidden/Tools |  |
| `microsoft_outlook` | Microsoft Outlook | Technisch/Brücke | Hidden |  |
| `onboarding` | Onboarding Toolbox | Technisch/Brücke | Hidden |  |
| `partner_autocomplete` | Partner Autocomplete | Technisch/Brücke | Hidden/Tools | Auto-complete partner companies' data |
| `payment` | Payment Engine | Technisch/Brücke | Hidden | The payment engine used by payment provider modules. |
| `phone_validation` | Phone Numbers Validation | Technisch/Brücke | Hidden | Validate and format phone numbers |
| `populate` | Populate | Technisch/Brücke | Hidden/Tools | Generate synthetic data for an Odoo database |
| `portal` | Customer Portal | Technisch/Brücke | Hidden | Customer Portal |
| `pos_sale_delivery` | POS - Sales Delivery | Technisch/Brücke | Hidden |  |
| `privacy_lookup` | Privacy | Technisch/Brücke | Hidden |  |
| `resource` | Resource | Technisch/Brücke | Hidden |  |
| `resource_mail` | Resource Mail | Technisch/Brücke | Hidden |  |
| `sale_project_stock_account` | Sale Project Stock Account | Technisch/Brücke | Hidden | Technical Bridge |
| `sms_twilio` | Twilio SMS | Technisch/Brücke | Hidden/Tools | Send SMS messages using Twilio |
| `snailmail` | Snail Mail | Technisch/Brücke | Hidden/Tools |  |
| `snailmail_account` | Snail Mail - Account | Technisch/Brücke | Hidden/Tools |  |
| `web` | Web | Technisch/Brücke | Hidden |  |
| `web_hierarchy` | Web Hierarchy | Technisch/Brücke | Hidden |  |
| `web_tour` | Tours | Technisch/Brücke | Hidden |  |
| `web_unsplash` | Unsplash Image Library | Technisch/Brücke | Hidden | Find free high-resolution images from Unsplash |

## Human Resources (27)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `fleet` | Fleet | App | Human Resources/Fleet | Manage your fleet and track car costs |
| `hr` | Employees | App | Human Resources/Employees | Centralize employee information |
| `hr_attendance` | Attendances | App | Human Resources/Attendances | Track employee attendance |
| `hr_expense` | Expenses | App | Human Resources/Expenses | Submit, validate and reinvoice employee expenses |
| `hr_holidays` | Time Off | App | Human Resources/Time Off | Allocate time off and follow leave requests |
| `hr_recruitment` | Recruitment | App | Human Resources/Recruitment | Track your recruitment pipeline |
| `hr_skills` | Skills Management | App | Human Resources/Employees | Manage skills, knowledge and resume of your employees |
| `lunch` | Lunch | App | Human Resources/Lunch | Handle lunch orders of your employees |
| `fleet_maintenance` | Maintenance - Fleet | Technisch/Brücke | Human Resources | Integrates Fleet and Maintenance |
| `gamification` | Gamification | Erweiterung | Human Resources |  |
| `hr_address_extended` | HR Address Extended | Erweiterung | Human Resources/Employees | Centralize employee information |
| `hr_calendar` | Display Working Hours in Calendar | Technisch/Brücke | Human Resources/Employees |  |
| `hr_calendar_google` | HR Calendar with Google Calendar | Technisch/Brücke | Human Resources/Remote Work |  |
| `hr_fleet` | Fleet History | Technisch/Brücke | Human Resources | Get history of driven cars by employees |
| `hr_gamification` | HR Gamification | Technisch/Brücke | Human Resources |  |
| `hr_holidays_attendance` | HR Attendance Holidays | Technisch/Brücke | Human Resources | Attendance Holidays |
| `hr_livechat` | HR - Livechat | Technisch/Brücke | Human Resources |  |
| `hr_maintenance` | Maintenance - HR | Technisch/Brücke | Human Resources | Equipment, Assets, Internal Hardware, Allocation Tracking |
| `hr_presence` | Employee Presence Control | Erweiterung | Human Resources |  |
| `hr_recruitment_skills` | Recruitment - Skills Management | Technisch/Brücke | Human Resources/Recruitment | Manage skills of your employees |
| `hr_recruitment_sms` | Recruitment - SMS | Technisch/Brücke | Human Resources/Recruitment | Mass mailing sms to job applicants |
| `hr_recruitment_survey` | Hr Recruitment Interview Forms | Erweiterung | Human Resources | Surveys |
| `hr_skills_slides` | Skills e-learning | Technisch/Brücke | Human Resources/Employees | Add completed courses to resume of your employees |
| `hr_skills_survey` | Skills Certification | Technisch/Brücke | Human Resources/Employees | Add certification to resume of your employees |
| `hr_timesheet_attendance` | Timesheets/attendances reporting | Technisch/Brücke | Human Resources/Attendances |  |
| `hr_work_entry` | Work Entries | Erweiterung | Human Resources/Employees | Manage work entries |
| `project_timesheet_holidays` | Timesheet when on Time Off | Technisch/Brücke | Human Resources | Schedule timesheet when on time off |

## Lokalisierung (Länder) (230)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `l10n_account_edi_ubl_cii_tests` | Testing the Import/Export invoices with UBL/CII | Lokalisierung | Accounting/Accounting |  |
| `l10n_account_withholding_tax` | Withholding Tax | Lokalisierung | Accounting/Localizations |  |
| `l10n_account_withholding_tax_pos` | Withholding Tax on Payment - PoS | Lokalisierung | Accounting/Localizations |  |
| `l10n_ae` | United Arab Emirates - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ae_pos` | United Arab Emirates - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_anz_ubl_pint` | Australia & New Zealand - UBL PINT | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_ar` | Argentina - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ar_pos` | Argentinean - Point of Sale with AR Doc | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_ar_stock` | Argentinean - Stock | Lokalisierung | Accounting/Localizations |  |
| `l10n_ar_website_sale` | Argentinean eCommerce | Lokalisierung | Accounting/Localizations/Website |  |
| `l10n_ar_withholding` | Argentina - Payment Withholdings | Lokalisierung | Accounting/Localizations |  |
| `l10n_at` | Austria - Accounting | Lokalisierung | Accounting/Localizations/Account Charts | Austrian Standardized Charts & Tax |
| `l10n_au` | Australia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_bd` | Bangladesh - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_be` | Belgium - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_be_pos` | BE POS Localization | Lokalisierung | Sales/Point of Sale | Link module between point_of_sale and l10n_be |
| `l10n_be_pos_restaurant` | Belgian POS Restaurant Localization | Lokalisierung | Sales/Point of Sale |  |
| `l10n_be_pos_sale` | l10n_be_pos_sale | Lokalisierung | Sales/Point of Sale | Link module between pos_sale and l10n_be |
| `l10n_bf` | Burkina Faso - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_bg` | Bulgaria - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_bg_ledger` | Bulgaria - Report ledger | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_bh` | Bahrain - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_bj` | Benin - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_bo` | Bolivia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_br` | Brazilian - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_br_sales` | Brazil - Sale | Lokalisierung | Sales/Sales |  |
| `l10n_br_website_sale` | Brazil - Website Sale | Lokalisierung | Sales/Sales |  |
| `l10n_ca` | Canada - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cd` | Democratic Republic of the Congo - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cf` | Central African Republic - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cg` | Congo - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ch` | Switzerland - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ch_pos` | Swiss - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_ci` | Ivory Coast - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cl` | Chile - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cm` | Cameroon - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cn` | China - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_co` | Colombia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_co_pos` | Colombian - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_cr` | Costa Rica - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cy` | Cyprus - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_cz` | Czech - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_de` | Germany - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_din5008` | DIN 5008 | Lokalisierung | Accounting/Localizations |  |
| `l10n_din5008_expense` | DIN 5008 - Expenses | Lokalisierung | Accounting/Localizations |  |
| `l10n_din5008_purchase` | DIN 5008 - Purchase | Lokalisierung | Accounting/Localizations |  |
| `l10n_din5008_repair` | DIN 5008 - Repair | Lokalisierung | Accounting/Localizations |  |
| `l10n_din5008_sale` | DIN 5008 - Sale | Lokalisierung | Accounting/Localizations |  |
| `l10n_din5008_stock` | DIN 5008 - Stock | Lokalisierung | Accounting/Localizations |  |
| `l10n_dk` | Denmark - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_dk_fik` | Denmark - FIK Number | Lokalisierung | Accounting/Localizations | Use FIK Number as Payment reference |
| `l10n_do` | Dominican Republic - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_dz` | Algeria - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ec` | Ecuadorian Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ec_sale` | Ecuador - Sale | Lokalisierung | Accounting/Localizations/Sale |  |
| `l10n_ee` | Estonia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_eg` | Egypt - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_eg_edi_eta` | Egypt E-Invoicing | Lokalisierung | account | Egypt Tax Authority Invoice Integration |
| `l10n_eg_edi_pos` | Egypt E-Receipts (POS) | Lokalisierung | Accounting/Localizations/EDI | Submit POS receipts to the Egyptian Tax Authority |
| `l10n_es` | Spain - Accounting (PGCE 2008) | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_es_edi_facturae` | Spain - Facturae EDI | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_es_edi_sii` | Spain - SII EDI Suministro de Libros | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_es_edi_tbai` | Spain - TicketBAI | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_es_edi_tbai_pos` | Spain - Point of Sale + TicketBAI | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_es_edi_verifactu` | Spain - Veri*Factu | Lokalisierung | Accounting/Localizations/EDI | Module for sending Spanish Veri*Factu XML to the AEAT |
| `l10n_es_edi_verifactu_pos` | Spain - Veri*Factu for Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale | Add Veri*Factu support to Point of Sale |
| `l10n_es_pos` | [Deprecated] Spain - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale | Spanish localization for Point of Sale |
| `l10n_es_website_sale` | Spain - ECommerce | Lokalisierung | Accounting/Localizations/Website |  |
| `l10n_et` | Ethiopia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_eu_account_vies` | VAT VIES Validation | Lokalisierung | Accounting/Accounting |  |
| `l10n_eu_oss` | EU One Stop Shop (OSS) | Lokalisierung | Accounting/Localizations |  |
| `l10n_fi` | Finland - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_fi_sale` | Finland - Sale | Lokalisierung | Sales/Sales |  |
| `l10n_fr` | France - Localizations | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_fr_account` | France - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_fr_facturx_chorus_pro` | France - BIS3 integration for Chorus Pro | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_fr_hr_holidays` | France - Time Off | Lokalisierung | Human Resources/Time Off | Management of leaves for part-time workers in France |
| `l10n_fr_payment` | France - Worldline Payment Branding | Lokalisierung | Uncategorized | Applies CAWL/Worldline branding rules for French companies. |
| `l10n_fr_pdp` | France - E-Invoicing (Approved Platform) | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_fr_pdp_pos` | France - E-reporting for POS | Lokalisierung | Accounting/Localizations/Reporting | Flux 10 e-reporting for POS |
| `l10n_fr_pos_cert` | France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis) | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_ga` | Gabon - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_gcc_invoice` | Gulf Cooperation Council - Invoice | Lokalisierung | Accounting/Localizations |  |
| `l10n_gcc_invoice_stock_account` | Gulf Cooperation Council WMS Accounting | Lokalisierung | Accounting/Localizations |  |
| `l10n_gcc_pos` | Gulf Cooperation Council - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_ge` | Georgia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts | Georgian accounting localization package |
| `l10n_gf` | Guyana - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_gn` | Guinea - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_gp` | Guadeloupe - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_gq` | Guinea Equatorial - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_gr` | Greece - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_gr_edi` | Greece - myDATA | Lokalisierung | Accounting/Localizations | Connect to myDATA API implementation for Greece |
| `l10n_gr_edi_delivery_note` | Greece - myDATA Delivery Note | Lokalisierung | Accounting/Localizations | Transmit Greece myDATA EDI for Delivery Notes |
| `l10n_gr_edi_e_invoo` | Greece - myDATA E-invoicing through e-invoo | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_gr_edi_e_invoo_bridge` | Greece - myDATA E-invoicing through e-invoo (direct API) | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_gt` | Guatemala - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_gw` | Guinea-Bissau - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_hk` | Hong Kong - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_hn` | Honduras - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_hr` | Croatia - Accounting (Euro) | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_hr_edi` | Croatia - e-invoicing | Lokalisierung | Accounting/Localizations/Reporting |  |
| `l10n_hr_kuna` | Croatia - Accounting (Kuna) | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_hu` | Hungary - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_hu_edi` | Hungary - E-invoicing | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_id` | Indonesian - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_id_efaktur_coretax` | Indonesia E-faktur (Coretax) | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_id_pos` | Indonesia - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_id_pos_self_order_qris` | Indonesia - POS Self Order QRIS | Lokalisierung | Sales/Point of Sale | Accept QRIS QR code payments in a kiosk. |
| `l10n_ie` | Ireland - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_il` | Israel - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_in` | Indian - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_in_boe` | Indian - Bill Of Entry | Lokalisierung | Accounting/Localizations |  |
| `l10n_in_edi` | Indian - E-invoicing | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_in_ewaybill` | Indian - E-waybill | Lokalisierung | Accounting/Localizations |  |
| `l10n_in_ewaybill_irn` | Indian - E-waybill thru IRN | Lokalisierung | Accounting/Localizations |  |
| `l10n_in_ewaybill_stock` | Indian - E-waybill Stock | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_in_hr_holidays` | India - Time Off | Lokalisierung | Human Resources/Time Off | Leave Management of Indian Localization |
| `l10n_in_pos` | Indian - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_in_purchase_stock` | India Purchase and Warehouse Management | Lokalisierung | Accounting/Localizations/Purchase | Get warehouse address if the bill is created from Purchase Order |
| `l10n_in_sale` | Indian - Sale Report(GST) | Lokalisierung | Accounting/Localizations/Sale |  |
| `l10n_in_sale_stock` | India Sales and Warehouse Management | Lokalisierung | Accounting/Localizations/Sale | Get warehouse address if the invoice is created from Sale Order |
| `l10n_in_stock` | Indian - Stock Report(GST) | Lokalisierung | Accounting/Localizations |  |
| `l10n_iq` | Iraq - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_it` | Italy - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_it_edi` | Italy - E-invoicing | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_it_edi_doi` | Italy - Declaration of Intent | Lokalisierung | Accounting/Localizations |  |
| `l10n_it_edi_sale` | Italy - Sale E-invoicing | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_it_stock_ddt` | Italy - Stock DDT | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_jo` | Jordan - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_jo_edi` | Jordan E-Invoicing | Lokalisierung | Accounting/Localizations/EDI | Electronic Invoicing for Jordan UBL 2.1 |
| `l10n_jo_edi_pos` | Jordan Accounting EDI for POS | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_jp` | Japan - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_jp_ubl_pint` | Japan - UBL PINT | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_ke` | Kenya - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ke_edi_tremol` | Kenya Tremol Device EDI Integration | Lokalisierung | Accounting/Localizations/EDI | Kenya Tremol Device EDI Integration |
| `l10n_kh` | Cambodia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_km` | Comoros - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_kr` | Republic of Korea - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_kr_sale` | Republic of Korea - Sales | Lokalisierung | Accounting/Localizations/Sale |  |
| `l10n_kw` | Kuwait - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_kz` | Kazakhstan - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_latam_check` | Third Party and Deferred/Electronic Checks Management | Lokalisierung | Accounting/Localizations | Checks Management |
| `l10n_latam_invoice_document` | LATAM Document | Lokalisierung | Accounting/Localizations | LATAM Document Types |
| `l10n_lb_account` | Lebanon - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_lk` | Sri Lanka - Accounting | Lokalisierung | Accounting/Localizations/Account Charts | Provides accounting localizations for Sri Lanka. |
| `l10n_lt` | Lithuania - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_lu` | Luxembourg - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_lv` | Latvia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ma` | Morocco - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mc` | Monaco - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mk` | North Macedonia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ml` | Mali - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mm` | Myanmar - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mn` | Mongolia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mq` | Martinique - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mr` | Mauritania - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mt` | Malta - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mt_pos` | Malta - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_mu_account` | Mauritius - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_mx` | Mexico - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_my` | Malaysia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_my_edi` | Malaysia - E-invoicing | Lokalisierung | Accounting/Localizations/EDI | E-invoicing using MyInvois |
| `l10n_my_edi_pos` | Malaysia - E-invoicing (POS) | Lokalisierung | Accounting/Localizations/EDI | Consolidated E-invoicing using MyInvois |
| `l10n_my_ubl_pint` | Malaysia - UBL PINT | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_mz` | Mozambique - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ne` | Niger - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ng` | Nigeria - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_nl` | Netherlands - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_no` | Norway - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_nz` | New Zealand - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_om` | Oman - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_pa` | Panama - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_pe` | Peru - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_pe_pos` | Peruvian - Point of Sale with Pe Doc | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_ph` | Philippines - Accounting | Lokalisierung | Accounting/Localizations/Account Charts | This is the module to manage the accounting chart for The Philippines. |
| `l10n_ph_invoice` | Philippines - Discount Privileges on Invoice | Lokalisierung | Accounting/Localizations | Apply Philippine SC/PWD discount privileges on customer invoices and credit notes. |
| `l10n_ph_sale` | Philippines - Discount Privileges on Sale Orders | Lokalisierung | Accounting/Localizations | Apply Philippine SC/PWD discount privileges on quotations and sale orders. |
| `l10n_pk` | Pakistan - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_pk_edi` | Pakistan - E-invoicing | Lokalisierung | Accounting/Localizations/EDI | Electronic Invoicing for Pakistan FBR(v1.12) |
| `l10n_pk_edi_pos` | Pakistan - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_pl` | Poland - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_pl_edi` | Polish E-Invoicing FA(3) | Lokalisierung | Accounting/Localizations | Support for FA(3) electronic invoices in Poland via KSeF |
| `l10n_pl_edi_jst` | Polish E-Invoicing FA(3) LGU support | Lokalisierung | Accounting/Localizations | Support for Local Government Unit (LGU) in the FA(3) format |
| `l10n_pt` | Portugal - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_qa` | Qatar - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_re` | Reunion - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ro` | Romania - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ro_edi` | Romania - E-invoicing | Lokalisierung | Accounting/Localizations/EDI | E-Invoice implementation for Romania |
| `l10n_ro_edi_stock` | Romania - E-Transport | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_rs` | Serbia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_rs_edi` | Serbia - eFaktura E-invoicing | Lokalisierung | Accounting/Localizations/EDI | E-Invoice implementation for Serbia |
| `l10n_rw` | Rwanda - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_sa` | Saudi Arabia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_sa_edi` | Saudi Arabia - E-invoicing | Lokalisierung | Accounting/Localizations/EDI | E-Invoicing, Universal Business Language |
| `l10n_sa_edi_pos` | Saudi Arabia - E-invoicing (Simplified) | Lokalisierung | Accounting/Localizations/EDI | ZATCA E-Invoicing, support for PoS |
| `l10n_sa_pos` | Saudi Arabia - Point of Sale | Lokalisierung | Accounting/Localizations/Point of Sale |  |
| `l10n_se` | Sweden - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_sg` | Singapore - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_sg_ubl_pint` | Singapore - UBL PINT | Lokalisierung | Accounting/Localizations/EDI |  |
| `l10n_si` | Slovenian - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_sk` | Slovak - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_sn` | Sénégal - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_syscohada` | OHADA - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_td` | Tchad - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_test_pos_qr_payment` | POS QR Tests | Lokalisierung | Sales/Point of Sale |  |
| `l10n_tg` | Togo - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_th` | Thailand - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_tn` | Tunisia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_tr` | Türkiye - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_tw` | Taiwan - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_tw_edi_ecpay` | Taiwan - E-invoicing | Lokalisierung | Accounting/Localizations/EDI | E-invoicing using ECpay |
| `l10n_tw_edi_ecpay_pos` | Taiwan - E-invoicing Pos | Lokalisierung | Point of sale/Localizations/EDI | ECpay E-invoice bridge module for POS |
| `l10n_tw_edi_ecpay_sale` | Taiwan - E-invoicing Sales | Lokalisierung | Website Sale/Localizations/EDI | ECPay E-invoice bridge module for Sales |
| `l10n_tw_edi_ecpay_website_sale` | Taiwan - E-invoicing Ecommerce | Lokalisierung | Website Sale/Localizations/EDI | ECpay E-invoice bridge module for Ecommerce |
| `l10n_tz_account` | Tanzania - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ua` | Ukraine - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ug` | Uganda - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_uk` | United Kingdom - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_us` | United States - Localizations | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_us_account` | United States - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_uy` | Uruguay - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_uz` | Uzbekistan - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_ve` | Venezuela - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_vn` | Vietnam - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_vn_edi_viettel` | Vietnam - E-invoicing | Lokalisierung | Accounting/Localizations/EDI | E-invoicing using SInvoice by Viettel |
| `l10n_vn_edi_viettel_pos` | Vietnam - POS E-invoicing | Lokalisierung | Accounting/Localizations/EDI | POS E-invoicing using SInvoice by Viettel |
| `l10n_vn_edi_viettel_stock` | Vietnam - Delivery E-invoicing | Lokalisierung | Accounting/Localizations/EDI | Delivery E-invoicing using SInvoice by Viettel |
| `l10n_yt` | Mayotte - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_za` | South Africa - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |
| `l10n_zm_account` | Zambia - Accounting | Lokalisierung | Accounting/Localizations/Account Charts |  |

## Marketing (39)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `marketing_card` | Marketing Card | App | Marketing/Marketing Card | Generate dynamic shareable cards |
| `mass_mailing` | Email Marketing | App | Marketing/Email Marketing | Design, send and track emails |
| `mass_mailing_sms` | SMS Marketing | App | Marketing/Email Marketing | Design, send and track SMS |
| `survey` | Surveys | App | Marketing/Surveys | Send your surveys or share them live. |
| `website_event` | Events | App | Marketing/Events | Publish events, sell tickets |
| `digest` | KPI Digests | Erweiterung | Marketing |  |
| `event` | Events Organization | Erweiterung | Marketing/Events | Trainings, Conferences, Meetings, Exhibitions, Registrations |
| `event_booth` | Events Booths | Erweiterung | Marketing/Events | Manage event booths |
| `event_booth_sale` | Events Booths Sales | Technisch/Brücke | Marketing/Events | Manage event booths sale |
| `event_crm` | Event CRM | Technisch/Brücke | Marketing/Events |  |
| `event_crm_sale` | Event CRM Sale | Technisch/Brücke | Marketing/Events |  |
| `event_product` | Events Product | Technisch/Brücke | Marketing/Events |  |
| `event_sale` | Events Sales | Technisch/Brücke | Marketing/Events |  |
| `event_sms` | SMS on Events | Technisch/Brücke | Marketing/Events |  |
| `link_tracker` | Link Tracker | Erweiterung | Marketing |  |
| `marketing_card_event` | Marketing Card For Events | Technisch/Brücke | Marketing/Marketing Card | Generate dynamic shareable cards for entities linked to events. |
| `mass_mailing_crm` | Mass mailing on lead / opportunities | Technisch/Brücke | Marketing/Email Marketing | Add lead / opportunities UTM info on mass mailing |
| `mass_mailing_crm_sms` | Mass mailing sms on lead / opportunities | Technisch/Brücke | Marketing/Email Marketing | Add lead / opportunities info on mass mailing sms |
| `mass_mailing_event` | Mass mailing on attendees | Technisch/Brücke | Marketing/Email Marketing |  |
| `mass_mailing_event_sms` | Event Attendees SMS Marketing | Technisch/Brücke | Marketing/Email Marketing |  |
| `mass_mailing_event_track` | Mass mailing on track speakers | Technisch/Brücke | Marketing/Email Marketing |  |
| `mass_mailing_event_track_sms` | Track Speakers SMS Marketing | Technisch/Brücke | Marketing/Email Marketing |  |
| `mass_mailing_sale` | Mass mailing on sale orders | Technisch/Brücke | Marketing/Email Marketing | Add sale order UTM info on mass mailing |
| `mass_mailing_sale_sms` | Mass mailing sms on sale orders | Technisch/Brücke | Marketing/Email Marketing | Add sale order info on mass mailing sms |
| `mass_mailing_slides` | Mass mailing on course members | Technisch/Brücke | Marketing/Email Marketing |  |
| `mass_mailing_themes` | Mass Mailing Themes | Technisch/Brücke | Marketing/Email Marketing | Design gorgeous mails |
| `social_media` | Social Media | Erweiterung | Marketing/Social Marketing | Social media connectors for company settings. |
| `survey_crm` | Survey CRM | Technisch/Brücke | Marketing/Surveys | Generate leads from surveys |
| `utm` | UTM Trackers | Erweiterung | Marketing |  |
| `website_event_booth` | Online Event Booths | Technisch/Brücke | Marketing/Events | Events, display your booths on your website |
| `website_event_booth_exhibitor` | Booths/Exhibitors Bridge | Technisch/Brücke | Marketing/Events | Event Booths, automatically create a sponsor. |
| `website_event_booth_sale` | Online Event Booth Sale | Technisch/Brücke | Marketing/Events | Events, sell your booths online |
| `website_event_booth_sale_exhibitor` | Booths Sale/Exhibitors Bridge | Technisch/Brücke | Marketing/Events | Bridge module between website_event_booth_exhibitor and website_event_booth_sale. |
| `website_event_exhibitor` | Event Exhibitors | Erweiterung | Marketing/Events | Event: manage sponsors and exhibitors |
| `website_event_track` | Advanced Events | Erweiterung | Marketing | Sponsors, Tracks, Agenda, Event News |
| `website_event_track_live` | Live Event Tracks | Erweiterung | Marketing/Events | Support live tracks: streaming, participation, youtube |
| `website_event_track_live_quiz` | Quiz on Live Event Tracks | Technisch/Brücke | Marketing/Events | Bridge module to support quiz features during "live" tracks. |
| `website_event_track_quiz` | Quizzes on Tracks | Erweiterung | Marketing/Events | Quizzes on tracks |
| `website_mass_mailing_event` | Mass mailing on website events | Technisch/Brücke | Marketing/Email Marketing/Website | Add pre-filled snippets in mass_mailing with an event snapshot |

## Productivity (28)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `calendar` | Calendar | App | Productivity/Calendar | Schedule employees' meetings |
| `data_recycle` | Data Recycle | App | Productivity/Data Cleaning | Find old records and archive/delete them |
| `mail` | Discuss | App | Productivity/Discuss | Chat, mail gateway and private channels |
| `project_todo` | To-Do | App | Productivity/To-Do | Organize your work with memos and to-do lists |
| `board` | Dashboards | Erweiterung | Productivity | Build your own dashboards |
| `calendar_sms` | Calendar - SMS | Technisch/Brücke | Productivity/Calendar | Send text messages as event reminders |
| `google_calendar` | Google Calendar | Erweiterung | Productivity |  |
| `mail_bot` | OdooBot | Technisch/Brücke | Productivity/Discuss | Add OdooBot in discussions |
| `mail_bot_hr` | OdooBot - HR | Technisch/Brücke | Productivity/Discuss | Bridge module between hr and mailbot. |
| `mail_tracking` | Discuss Tracking | Erweiterung | Productivity/Discuss | Technical tracking of discussion and message-related data |
| `mail_tracking_mass_mailing` | Mass Mailing Tracking | Technisch/Brücke | Productivity/Discuss | Track source of messages by mass mailing |
| `mail_tracking_sms` | SMS Message Tracking | Technisch/Brücke | Productivity/Discuss | Track source of messages by sms |
| `microsoft_calendar` | Outlook Calendar | Erweiterung | Productivity |  |
| `rating` | Customer Rating | Erweiterung | Productivity |  |
| `spreadsheet` | Spreadsheet | Erweiterung | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard` | Spreadsheet dashboard | Erweiterung | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_account` | Spreadsheet dashboard for accounting | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_event_sale` | Spreadsheet dashboard for events | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_hr_expense` | Spreadsheet dashboard for expenses | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_hr_timesheet` | Spreadsheet dashboard for time sheets | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_im_livechat` | Spreadsheet dashboard for live chat | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_pos_hr` | Spreadsheet dashboard for point of sale | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_pos_restaurant` | Spreadsheet dashboard for restaurants | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_sale` | Spreadsheet dashboard for sales | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_sale_timesheet` | Spreadsheet dashboard for time sheets | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_stock_account` | Spreadsheet dashboard for stock | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_website_sale` | Spreadsheet dashboard for eCommerce | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |
| `spreadsheet_dashboard_website_sale_slides` | Spreadsheet dashboard for eLearning | Technisch/Brücke | Productivity/Dashboard | Spreadsheet |

## Sales (92)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `contacts` | Contacts | App | Sales/CRM | Centralize your address book |
| `crm` | CRM | App | Sales/CRM | Track leads and close opportunities |
| `point_of_sale` | Point of Sale | App | Sales/Point of Sale | Handle checkouts and payments for shops and restaurants. |
| `pos_restaurant` | Restaurant | App | Sales/Point of Sale | Restaurant extensions for the Point of Sale |
| `sale_management` | Sales | App | Sales/Sales | From quotations to invoices |
| `base_address_extended` | Extended Addresses | Erweiterung | Sales/Sales | Add extra fields on addresses |
| `base_automation` | Automation Rules | Erweiterung | Sales/Sales |  |
| `base_geolocalize` | Partners Geolocation | Erweiterung | Sales/Sales |  |
| `crm_iap_enrich` | Lead Enrichment | Technisch/Brücke | Sales/CRM | Enrich Leads/Opportunities using email address domain |
| `crm_iap_mine` | Lead Generation | Technisch/Brücke | Sales/CRM | Generate Leads/Opportunities based on country, industries, size, etc. |
| `crm_livechat` | CRM Livechat | Technisch/Brücke | Sales/CRM | Create lead from livechat conversation |
| `crm_mail_plugin` | CRM Mail Plugin | Technisch/Brücke | Sales/CRM | Turn emails received in your mailbox into leads and log their content as internal notes. |
| `crm_sale_project` | CRM - Project | Technisch/Brücke | Sales/CRM | Project Generation from Opportunities |
| `crm_sms` | SMS in CRM | Technisch/Brücke | Sales/CRM | Add SMS capabilities to CRM |
| `delivery` | Delivery Costs | Erweiterung | Sales/Delivery |  |
| `gamification_sale_crm` | CRM Gamification | Technisch/Brücke | Sales/CRM |  |
| `loyalty` | Coupons & Loyalty | Erweiterung | Sales | Use discounts, gift cards, eWallets and loyalty programs in your sales channels |
| `mail_plugin` | Mail Plugin | Technisch/Brücke | Sales/CRM | Allows integration with mail plugins. |
| `mysubscription` | My Subscription | Technisch/Brücke | Sales | Backend Subscription App |
| `partnership` | Partnership / Membership | Erweiterung | Sales/CRM |  |
| `pos_adyen` | POS Adyen | Erweiterung | Sales/Point of Sale | Integrate your POS with an Adyen payment terminal |
| `pos_bancontact_pay` | POS Bancontact Pay & Wero | Erweiterung | Sales/Point of Sale | Accept Bancontact Pay and Wero QR code payments in POS (Payconiq). |
| `pos_cashdro` | POS Cashdro Cash Machines | Erweiterung | Sales/Point of Sale | Integrate your POS with a Cashdro automatic cash payment device |
| `pos_cashmatic` | POS Cashmatic Cash Machines | Erweiterung | Sales/Point of Sale | Integrate your POS with a cash matic automatic cash payment device |
| `pos_discount` | Point of Sale Discounts | Erweiterung | Sales/Point of Sale | Simple Discounts in the Point of Sale |
| `pos_dpopay` | PoS DPO Pay | Erweiterung | Sales/Point of Sale | Integrate your POS with DPO payment terminal. |
| `pos_edi_ubl` | Point of Sale UBL | Erweiterung | Sales/Point of Sale | UBL in the Point of Sale |
| `pos_glory_cash` | POS Glory Cash Machines | Erweiterung | Sales/Point of Sale | Integrate your POS with a Glory automatic cash payment device |
| `pos_hr` | POS - HR | Technisch/Brücke | Sales/Point of Sale | Link module between Point of Sale and HR |
| `pos_hr_restaurant` | POS HR Restaurant | Technisch/Brücke | Sales/Point of Sale | Link module between pos_hr and pos_restaurant |
| `pos_imin` | POS iMin | Erweiterung | Sales/Point of Sale | iMin ePOS Printers in PoS |
| `pos_loyalty` | Point of Sale - Coupons & Loyalty | Technisch/Brücke | Sales/Point Of Sale | Use Coupons, Gift Cards and Loyalty programs in Point of Sale |
| `pos_mercado_pago` | POS Mercado Pago | Erweiterung | Sales/Point of Sale | Integrate your POS with the Mercado Pago Smart Point terminal |
| `pos_mollie` | POS Mollie | Erweiterung | Sales/Point of Sale | Integrate your POS with a Mollie payment terminal |
| `pos_mrp` | pos_mrp | Technisch/Brücke | Sales/Point of Sale | Link module between Point of Sale and Mrp |
| `pos_online_payment_self_order` | POS Self-Order / Online Payment | Technisch/Brücke | Sales/Point of Sale | Support online payment in self-order |
| `pos_partner_autocomplete` | POS Partner Autocomplete | Technisch/Brücke | Sales/Point of Sale | Link module between Partner Autocomplete and Point of Sale |
| `pos_pine_labs` | POS Pine Labs | Erweiterung | Sales/Point of Sale | Integrate your POS with Pine Labs payment terminals |
| `pos_qfpay` | POS QFPay | Erweiterung | Sales/Point of Sale | Integrate your POS with the QFPay terminal in Hong Kong |
| `pos_razorpay` | POS Razorpay | Erweiterung | Sales/Point of Sale | Integrate your POS with a Razorpay payment terminal |
| `pos_restaurant_loyalty` | POS - Restaurant Loyalty | Technisch/Brücke | Sales/Point of Sale | Link module between pos_restaurant and pos_loyalty |
| `pos_safaricom` | POS Safaricom | Erweiterung | Sales/Point of Sale | Integrate your POS with the Safaricom Payment Provider |
| `pos_sale` | POS - Sales | Technisch/Brücke | Sales/Point of Sale | Link module between Point of Sale and Sales |
| `pos_sale_loyalty` | POS - Sales Loyalty | Technisch/Brücke | Sales/Point of Sale | Link module between pos_sale and pos_loyalty |
| `pos_sale_margin` | POS - Sale Margin | Technisch/Brücke | Sales/Point of Sale | Link module between Point of Sale and Sales Margin |
| `pos_sale_stock` | POS - Sales Stock | Technisch/Brücke | Sales/Point of Sale | Link module between PoS Stock and Sales |
| `pos_self_order` | POS Self Order | Technisch/Brücke | Sales/Point Of Sale | Addon for the POS App that allows customers to view the menu on their smartphone. |
| `pos_self_order_bancontact_pay` | POS Self Order Bancontact Pay & Wero | Technisch/Brücke | Sales/Point of Sale | Accept Bancontact Pay and Wero QR code payments in a kiosk (Payconiq). |
| `pos_self_order_event` | POS Self Order - Event | Technisch/Brücke | Sales/Point Of Sale | Link module between PoS Self Order and PoS Event |
| `pos_self_order_pine_labs` | POS Self Order Pine Labs | Technisch/Brücke | Sales/Point Of Sale | An addon for the Self Order App (KIOSK) that allows customers to pay using the Pine Labs POS Terminal. |
| `pos_self_order_qfpay` | POS Self Order QFPay | Technisch/Brücke | Sales/Point Of Sale | Addon for the Self Order App that allows customers to pay by QFPay. |
| `pos_self_order_razorpay` | POS Self Order Razorpay | Technisch/Brücke | Sales/Point Of Sale | Addon for the Self Order App that allows customers to pay by Razorpay POS Terminal. |
| `pos_self_order_sale` | POS Self Order Sale | Technisch/Brücke | Sales/Point Of Sale |  |
| `pos_self_order_sms` | POS Self Order SMS | Technisch/Brücke | Sales/Point Of Sale |  |
| `pos_stock` | PoS - Stock | Technisch/Brücke | Sales/Point of Sale | Stock integration for PoS |
| `pos_stripe` | POS Stripe | Erweiterung | Sales/Point of Sale | Integrate your POS with a Stripe payment terminal |
| `pos_sumup` | POS SumUp | Erweiterung | Sales/Point of Sale | Integrate your POS with a SumUp payment terminal |
| `pos_viva_com` | PoS Viva.com | Erweiterung | Sales/Point of Sale | Integrate your PoS with a Viva.com payment terminal |
| `product` | Products & Pricelists | Erweiterung | Sales/Sales |  |
| `product_margin` | Margins by Products | Erweiterung | Sales/Sales |  |
| `product_matrix` | Product Matrix | Erweiterung | Sales/Sales | Technical module: Matrix Implementation |
| `sale` | Sales | Erweiterung | Sales/Sales | Sales internal machinery |
| `sale_crm` | Opportunity to Quotation | Technisch/Brücke | Sales/Sales |  |
| `sale_edi_ubl` | Import electronic orders with UBL | Technisch/Brücke | Sales/Sales |  |
| `sale_expense` | Sales Expense | Technisch/Brücke | Sales/Sales | Quotation, Sales Orders, Delivery & Invoicing Control |
| `sale_expense_margin` | Sales Expense Margin | Technisch/Brücke | Sales/Sales |  |
| `sale_gelato` | Gelato | Erweiterung | Sales/Sales | Place orders through Gelato's print-on-demand service |
| `sale_gelato_stock` | Gelato/Stock bridge | Technisch/Brücke | Sales/Sales |  |
| `sale_loyalty` | Sale Loyalty | Technisch/Brücke | Sales/Sales | Use discounts and loyalty programs in sales orders |
| `sale_loyalty_delivery` | Sale Loyalty - Delivery | Technisch/Brücke | Sales/Sales | Adds free shipping mechanism in sales orders |
| `sale_margin` | Margins in Sales Orders | Technisch/Brücke | Sales/Sales |  |
| `sale_mrp` | Sales and MRP Management | Technisch/Brücke | Sales/Sales |  |
| `sale_mrp_margin` | Sale Mrp Margin | Erweiterung | Sales/Sales |  |
| `sale_pdf_quote_builder` | Sales PDF Quotation Builder | Technisch/Brücke | Sales/Sales |  |
| `sale_product_matrix` | Sale Matrix | Erweiterung | Sales/Sales | Add variants to Sales Order through a grid entry. |
| `sale_project` | Sales - Project | Technisch/Brücke | Sales/Sales | Task Generation from Sales Orders |
| `sale_project_margin` | Sales Margins in Projects | Technisch/Brücke | Sales/Sales | Bridge module between Sales Margin and Project |
| `sale_project_stock` | Sale Project - Sale Stock | Technisch/Brücke | Sales | Adds a full traceability of inventory operations on the profitability report. |
| `sale_purchase` | Sale Purchase | Technisch/Brücke | Sales/Sales | Sale based on service outsourcing. |
| `sale_purchase_project` | Sale Purchase Project | Technisch/Brücke | Sales | Technical Bridge |
| `sale_purchase_stock` | MTO Sale <-> Purchase | Technisch/Brücke | Sales/Sales | SO/PO relation in case of MTO |
| `sale_service` | Sales - Service | Erweiterung | Sales/Sales | Interaction between Sales and services apps (project and planning) |
| `sale_sms` | Sale - SMS | Technisch/Brücke | Sales/Sales | Ease SMS integration with sales capabilities |
| `sale_stock` | Sales and Warehouse Management | Technisch/Brücke | Sales/Sales | Quotation, Sales Orders, Delivery & Invoicing Control |
| `sale_stock_margin` | Sale Stock Margin | Technisch/Brücke | Sales/Sales |  |
| `sale_stock_product_expiry` | Sale Stock Product Expiry | Technisch/Brücke | Sales/Sales |  |
| `sale_timesheet` | Sales Timesheet | Technisch/Brücke | Sales/Sales | Sell based on timesheets |
| `sale_timesheet_margin` | Service Margins in Sales Orders | Technisch/Brücke | Sales/Sales | Bridge module between Sales Margin and Sales Timesheet |
| `sales_team` | Sales Teams | Erweiterung | Sales/Sales | Sales Teams |
| `sms` | SMS gateway | Technisch/Brücke | Sales/Sales | SMS Text Messaging |
| `uom` | Units of measure | Erweiterung | Sales/Sales |  |
| `website_crm_iap_reveal` | Lead Generation From Website Visits | Erweiterung | Sales/CRM | Generate Leads/Opportunities from your website's traffic |

## Send sms to customer for order confirmation (1)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `pos_sms` | POS - SMS | Erweiterung | Send sms to customer for order confirmation |  |

## Services (16)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `project` | Project | App | Services/Project | Manage tasks and collaborate on projects |
| `hr_timesheet` | Task Logs | Erweiterung | Services/Timesheets | Track employee time on tasks |
| `portal_discuss` | Portal Discuss | Technisch/Brücke | Services |  |
| `portal_rating` | Portal Rating | Technisch/Brücke | Services |  |
| `project_hr_expense` | Project Expenses | Technisch/Brücke | Services/expenses | Project expenses |
| `project_hr_skills` | Project - Skills | Technisch/Brücke | Services/Project | Project skills |
| `project_mail_plugin` | Project Mail Plugin | Technisch/Brücke | Services/Project | Integrate your inbox with projects |
| `project_mrp` | MRP Project | Technisch/Brücke | Services/Project | Monitor MRP using project |
| `project_mrp_account` | MRP Account Project | Technisch/Brücke | Services/Project | Monitor MRP account using project |
| `project_mrp_sale` | MRP Project Sale | Technisch/Brücke | Services/Project | Technical Bridge |
| `project_purchase` | Project Purchase | Technisch/Brücke | Services/Project | Monitor purchase in project |
| `project_purchase_stock` | Project - Purchase - Stock | Technisch/Brücke | Services/Project |  |
| `project_sale_expense` | Project - Sale - Expense | Technisch/Brücke | Services/Project |  |
| `project_sms` | Project - SMS | Technisch/Brücke | Services/Project | Send text messages when project/task stage move |
| `project_stock` | Project Stock | Technisch/Brücke | Services/Project | Link Stock pickings to Project |
| `project_stock_account` | Project Stock Account | Technisch/Brücke | Services/Project | Handle analytics in Stock pickings with Project |

## Shipping Connectors (2)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `mrp_delivery` | Delivery and MRP Management | Technisch/Brücke | Shipping Connectors | Carrier with kits |
| `stock_delivery` | Delivery - Stock | Technisch/Brücke | Shipping Connectors |  |

## Supply Chain (34)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `maintenance` | Maintenance | App | Supply Chain/Maintenance | Track equipment and manage maintenance requests |
| `mrp` | Manufacturing | App | Supply Chain/Manufacturing | Manufacturing Orders & BOMs |
| `purchase` | Purchase | App | Supply Chain/Purchase | Purchase orders, tenders and agreements |
| `repair` | Repairs | App | Supply Chain/Inventory | Repair damaged products |
| `stock` | Inventory | App | Supply Chain/Inventory | Manage your stock and logistics activities |
| `barcodes` | Barcode | Erweiterung | Supply Chain/Inventory | Scan and Parse Barcodes |
| `barcodes_gs1_nomenclature` | Barcode - GS1 Nomenclature | Erweiterung | Supply Chain/Inventory | Parse barcodes according to the GS1-128 specifications |
| `mrp_account` | Accounting - MRP | Technisch/Brücke | Supply Chain/Manufacturing | Analytic accounting in Manufacturing |
| `mrp_landed_costs` | Landed Costs On MO | Technisch/Brücke | Supply Chain/Manufacturing | Landed Costs on Manufacturing Order |
| `mrp_product_expiry` | Manufacturing Expiry | Technisch/Brücke | Supply Chain/Manufacturing | Manufacturing Expiry |
| `mrp_repair` | Mrp Repairs | Technisch/Brücke | Supply Chain/Inventory |  |
| `mrp_subcontracting` | MRP Subcontracting | Erweiterung | Supply Chain/Manufacturing | Subcontract Productions |
| `mrp_subcontracting_account` | Subcontracting Management with Stock Valuation | Technisch/Brücke | Supply Chain/Manufacturing |  |
| `mrp_subcontracting_dropshipping` | Dropship and Subcontracting Management | Technisch/Brücke | Supply Chain/Purchase |  |
| `mrp_subcontracting_landed_costs` | Landed Costs With Subcontracting order | Technisch/Brücke | Supply Chain/Manufacturing | Advanced views to manage landed cost for subcontracting orders |
| `mrp_subcontracting_purchase` | Purchase and Subcontracting Management | Technisch/Brücke | Supply Chain/Purchase |  |
| `product_expiry` | Products Expiration Date | Erweiterung | Supply Chain/Inventory |  |
| `project_mrp_stock_landed_costs` | Project MRP Landed Costs | Technisch/Brücke | Supply Chain/Manufacturing | Technical Bridge |
| `project_stock_landed_costs` | Project Stock Landed Costs | Technisch/Brücke | Supply Chain/Inventory | Technical Bridge |
| `purchase_alternative` | Purchase Alternative | Erweiterung | Supply Chain/Purchase |  |
| `purchase_alternative_sale` | Purchase Alternative Sale | Technisch/Brücke | Supply Chain/Purchase |  |
| `purchase_alternative_stock` | Purchase Alternative Stock | Technisch/Brücke | Supply Chain/Purchase |  |
| `purchase_edi_ubl_bis3` | Import/Export electronic orders with UBL | Technisch/Brücke | Supply Chain/Purchase |  |
| `purchase_mrp` | Purchase and MRP Management | Technisch/Brücke | Supply Chain/Purchase |  |
| `purchase_product_matrix` | Purchase Matrix | Erweiterung | Supply Chain/Purchase | Add variants to your purchase orders through an Order Grid Entry. |
| `purchase_repair` | Purchase Repair | Technisch/Brücke | Supply Chain/Purchase | Keep track of linked purchase and repair orders |
| `purchase_requisition` | Purchase Agreements | Erweiterung | Supply Chain/Purchase |  |
| `purchase_requisition_stock` | Purchase Requisition Stock | Technisch/Brücke | Supply Chain/Purchase |  |
| `purchase_stock` | Purchase Stock | Technisch/Brücke | Supply Chain/Purchase | Purchase Orders, Receipts, Vendor Bills for Stock |
| `stock_account` | WMS Accounting | Technisch/Brücke | Supply Chain/Inventory | Inventory, Logistic, Valuation, Accounting |
| `stock_dropshipping` | Drop Shipping | Erweiterung | Supply Chain/Inventory | Drop Shipping |
| `stock_landed_costs` | WMS Landed Costs | Erweiterung | Supply Chain/Inventory | Landed Costs |
| `stock_maintenance` | Stock - Maintenance | Technisch/Brücke | Supply Chain/Inventory | See lots used in maintenance |
| `stock_sms` | Stock - SMS | Technisch/Brücke | Supply Chain/Inventory | Send text messages when final stock move |

## Technical (3)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `pos_event` | POS - Event | Technisch/Brücke | Technical | Link module between Point of Sale and Event |
| `pos_event_sale` | PoS - Event Sale | Technisch/Brücke | Technical | Link module between pos_sale and pos_event |
| `pos_repair` | POS - Repair | Technisch/Brücke | Technical | Link module between Point of Sale and Repair |

## Technical Settings (4)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `cloud_storage` | Cloud Storage | Technisch/Brücke | Technical Settings | Store chatter attachments in the cloud |
| `cloud_storage_azure` | Cloud Storage Azure | Technisch/Brücke | Technical Settings | Store chatter attachments in the Azure cloud |
| `cloud_storage_google` | Cloud Storage Google | Technisch/Brücke | Technical Settings | Store chatter attachments in the Google cloud |
| `cloud_storage_migration` | Cloud Storage Migration | Technisch/Brücke | Technical Settings | Migrate local attachments to cloud storage |

## Theme (1)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `theme_default` | Default Theme | Erweiterung | Theme |  |

## Tools (1)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `auth_password_policy_portal` | Password Policy support for Signup | Technisch/Brücke | Tools |  |

## Uncategorized (6)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `html_builder` | HTML Builder | Erweiterung | Uncategorized | Generic html builder |
| `mail_group` | Mail Group | Erweiterung | Uncategorized | Manage your mailing lists |
| `pos_online_payment` | Point of Sale online payment | Technisch/Brücke | Uncategorized |  |
| `printer` | Printer | Erweiterung | Uncategorized | Base module to manage external printers (e.g. ePOS, ZPL) |
| `stock_fleet` | Stock Transport | Erweiterung | Uncategorized | Stock Transport Management |
| `website_mail_group` | Website Mail Group | Technisch/Brücke | Uncategorized | Add a website snippet for the mail groups. |

## Website (40)

| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |
|---|---|---|---|---|
| `im_livechat` | Live Chat | App | Website/Live Chat | Chat with your website visitors |
| `website` | Website | App | Website/Website | Enterprise website builder |
| `website_hr_recruitment` | Online Jobs | App | Website/Website | Manage your online hiring process |
| `website_sale` | eCommerce | App | Website/Website | Sell your products online |
| `website_slides` | eLearning | App | Website/eLearning | Manage and publish an eLearning platform |
| `website_address_autocomplete` | Website Address Autocomplete | Technisch/Brücke | Website/Website | Assist your users with automatic completion & suggestions when filling their address |
| `website_blog` | Blog | Erweiterung | Website/Website | Publish blog posts, announces, news |
| `website_cf_turnstile` | Cloudflare Turnstile | Erweiterung | Website/Website |  |
| `website_crm` | Contact Form | Technisch/Brücke | Website/Website | Generate leads from a contact form |
| `website_crm_livechat` | Lead Livechat Sessions | Technisch/Brücke | Website/Website | View livechat sessions for leads |
| `website_crm_partner_assign` | Resellers | Erweiterung | Website/Website | Publish your resellers/partners and forward leads to them |
| `website_crm_sms` | Send SMS to Visitor with leads | Technisch/Brücke | Website/Website | Allows to send sms to website visitor that have lead |
| `website_customer` | Customer References | Erweiterung | Website/Website | Publish your customer references |
| `website_event_crm` | Website Events CRM | Technisch/Brücke | Website/Website |  |
| `website_event_sale` | Online Event Ticketing | Technisch/Brücke | Website/Website | Sell event tickets online |
| `website_forum` | Forum | Erweiterung | Website/Website | Manage a forum with FAQ and Q&A |
| `website_google_map` | Google Maps | Erweiterung | Website/Website | Show your company address on Google Maps |
| `website_hr_recruitment_livechat` | Website IM Livechat HR Recruitment | Erweiterung | Website/Live Chat | Chatbot for the HR Recruitment |
| `website_links` | Link Tracker | Technisch/Brücke | Website/Website | Generate trackable & short URLs |
| `website_livechat` | Website Live Chat | Technisch/Brücke | Website/Live Chat | Chat with your website visitors |
| `website_mail` | Website Mail | Technisch/Brücke | Website/Website | Website Module for Mail |
| `website_mass_mailing` | Newsletter Subscribe Button | Technisch/Brücke | Website/Website | Attract visitors to subscribe to mailing lists |
| `website_mass_mailing_sms` | Newsletter Subscribe SMS Template | Technisch/Brücke | Website/Website | Attract visitors to subscribe to mailing lists |
| `website_partner` | Website Partner | Erweiterung | Website/Website | Partner module for website |
| `website_partnership` | Website Partnership | Erweiterung | Website/Website | Publish your partners on your website |
| `website_payment` | Website Payment | Technisch/Brücke | Website/Website | Payment integration with website |
| `website_profile` | Website profile | Erweiterung | Website/Website | Access the website profile of the users |
| `website_project` | Online Task Submission | Technisch/Brücke | Website/Website | Add a task suggestion form to your website |
| `website_sale_collect` | Click & Collect | Erweiterung | Website/Website |  |
| `website_sale_gelato` | eCommerce/Gelato bridge | Technisch/Brücke | Website/Website |  |
| `website_sale_loyalty` | Coupons, Promotions, Gift Card and Loyalty for eCommerce | Technisch/Brücke | Website/Website | Use coupon, promotion, gift cards and loyalty programs in your eCommerce store |
| `website_sale_mass_mailing` | Checkout Newsletter | Technisch/Brücke | Website/Website | Let new customers sign up for a newsletter during checkout |
| `website_sale_mrp` | Kit Availability | Technisch/Brücke | Website/Website | Manage Kit product inventory & availability |
| `website_sale_project` | Website Sale - Project | Technisch/Brücke | Website/Website | Bridge module between website_sale and project |
| `website_sale_slides` | Sell Courses | Erweiterung | Website/eLearning | Sell your courses online |
| `website_sale_stock` | Product Availability | Technisch/Brücke | Website/Website | Manage product inventory & availability |
| `website_slides_forum` | Forum on Courses | Technisch/Brücke | Website/eLearning | Allows to link forum on a course |
| `website_slides_survey` | Course Certifications | Technisch/Brücke | Website/eLearning | Add certification capabilities to your courses |
| `website_sms` | Send SMS to Visitor | Technisch/Brücke | Website/Website | Allows to send sms to website visitor |
| `website_timesheet` | Hide Portal Timesheet Information | Technisch/Brücke | Website/Website | Allow hiding timesheet information in the portal |
