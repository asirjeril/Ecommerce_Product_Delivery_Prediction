def test_import():
    import src.ecommerce_delivery as pkg
    assert hasattr(pkg, "__version__")
