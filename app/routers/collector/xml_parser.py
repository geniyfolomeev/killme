import lxml
from lxml import etree
from lxml.etree import _Element


class InvalidXml(Exception):
    pass


def _to_float(value: str) -> float:
    return round(float(value) * 100, 2)


def file_to_xml(content) -> _Element:
    try:
        return etree.fromstring(content)
    except lxml.etree.XMLSyntaxError:
        raise InvalidXml("Невалидный xml файл")


def find_handlers_coverage(root_element: _Element, handlers: set[str]) -> dict:
    cov = {"total": _to_float(root_element.get("line-rate", 0)), "handlers": []}

    # Находим все методы с атрибутом name, соответствующим именам хендлеров
    methods = root_element.findall(".//method[@name]")
    for method_element in methods:
        method_name = method_element.get("name")
        if method_name in handlers:
            # Находим класс, к которому принадлежит метод
            class_element = method_element.getparent().getparent()
            # Проверяем, содержит ли класс атрибут filename, содержащий подстроку 'internal/app'
            if 'internal/app' in class_element.get("filename", ""):
                line_rate = _to_float(method_element.get("line-rate", 0))
                cov["handlers"].append({method_name: line_rate})

    return cov
