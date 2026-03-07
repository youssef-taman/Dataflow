SELECT 

    l.l_orderkey AS order_key,
    l.l_linenumber AS line_number,
    o.o_custkey AS cust_key,
    l.l_suppkey AS supp_key,
    l.l_partkey AS part_key,

    l.l_shipdate AS ship_date,
    l.l_commitdate AS commit_date,
    l.l_receiptdate AS receipt_date,
    o.o_orderdate AS order_date,

    l.l_quantity AS quantity,
    l.l_extendedprice AS extended_price,
    l.l_discount AS discount,
    l.l_tax AS tax,

    o.o_orderstatus AS order_status,
    o.o_orderpriority AS order_priority,
    o.o_clerk AS clerk,
    l.l_returnflag AS return_flag,
    l.l_linestatus AS line_status,
    l.l_shipinstruct AS ship_instructions,
    l.l_shipmode AS ship_mode

FROM lineitem l
JOIN orders o ON l.l_orderkey = o.o_orderkey;