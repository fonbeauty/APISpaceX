import allure
from xmlschema import XMLSchemaChildrenValidationError

from templates.read_templates import country_iso_code_xml, xsd_response, country_name_xml
from templates.utils import check_result_operation


@allure.feature('SOAP')
class TestPeople:
    @allure.story('Positive tests')
    class TestPositive:

        def test_country_name_service(self, soap_session):
            response = soap_session.request(method='POST', data=country_iso_code_xml('IT'))
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/soap+xml; charset=utf-8'

            try:
                xsd_response('CountryNameResponse').validate(response.text)
            except XMLSchemaChildrenValidationError as xml_e:
                raise AssertionError(xml_e)
            # assert country_iso_code_xsd_response.is_valid(response.text)

            assert check_result_operation(response.text, 'Italy')

            # root = ET.fromstring(response.text)
            # assert root[0][0][0].text == 'Italy'
            # assert 'CountryNameResult' in root[0][0][0].tag

            pass


        def test_country_iso_service(self, soap_session):
            response = soap_session.request(method='POST', data=country_name_xml('Italy'))
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/soap+xml; charset=utf-8'

            try:
                xsd_response('CountryISOCodeResponse').validate(response.text)
            except XMLSchemaChildrenValidationError as xml_e:
                raise AssertionError(xml_e)

            assert check_result_operation(response.text, 'IT')
            # root = ET.fromstring(response.text)
            # assert root[0][0][0].text == 'IT'
