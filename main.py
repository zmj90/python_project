import re

l1 = [1, 2, 3]
l2 = ["1001", "2", "3"]
l3 = ["1001", "2", "3"]
print(l1 == l2)
print(l2 == l3)
s1 = r"""
{
    "data": "[
        {\"vend_id\": 1001, \"vend_name\": \"Anvils R Us\"}, 
        {\"vend_id\": 1002, \"vend_name\": \"LT Supplies\"}, 
        {\"vend_id\": 1003, \"vend_name\": \"ACME\"}]",
    "json": [
        {
            "vend_id1": 1001,
            "vend_name": "Anvils R Us"
        },
        {
            "vend_id1": 1002,
            "vend_name": "LT Supplies"
        },
        {
            "vend_id": 1003,
            "vend_name": "ACME"
        }
    ]
}
"""
_ = re.findall(r'"vend_id": (\d+)', s1)
print(_, type(_))
