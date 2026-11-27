ALTER TABLE `games` ADD `daily` integer DEFAULT false NOT NULL;
--> statement-breakpoint
-- 한 판에 구간 5개(누적) → 3개(겹치지 않음): 5분 이하 → 10분 안쪽, 15·30분 이하 → 10~30분, 1시간 이하 · 넘게 → 30분 이상
UPDATE `games` SET `length` = CASE WHEN `length` <= 1 THEN 1 WHEN `length` <= 3 THEN 2 ELSE 3 END;
