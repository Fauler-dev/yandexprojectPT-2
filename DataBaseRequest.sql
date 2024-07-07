# Заврикиди Глеб, 18 когорта — Дипломный проект. Инженер по тестированию +

# Вывод логино курьеров с заказами в статусе «В доставке» (поле inDelivery = true).

SELECT c.login,
       COUNT(o.*) AS order_count
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

# Вывод статусов заказов без привязки к курьеру

SELECT track,
          CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
  ELSE 0 END AS status
      FROM "Orders";