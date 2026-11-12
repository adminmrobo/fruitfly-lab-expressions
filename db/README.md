# 캐릭터 DB (엑셀) — 판별 보관

캐릭터 벡터(표정·동작·헤어·3D 등)가 바뀔 때마다 새 판을 **추가**합니다. 이전 판은 지우거나 덮어쓰지 않습니다.

- 파일 이름: `fruitfly_character_db_v{판}_{YYYY-MM-DD}.xlsx`
- 가장 최신 판: 아래 표의 맨 아래 줄
- 원본 원칙: 메타데이터·상태·사용 이력은 엑셀이 원본, 그림 파일과 변경 이력은 이 저장소가 원본 (시트 → 저장소 한 방향)

| 판 | 날짜 | 파일 | 바뀐 내용 |
|---|---|---|---|
| v1.0 | 2026-11-11 | [fruitfly_character_db_v1.0_2026-11-11.xlsx](fruitfly_character_db_v1.0_2026-11-11.xlsx) | 첫판: characters · expressions(216) · motion_sheets(59) · motion_segments(127) · usage · 코드표 |
| v1.1 | 2026-11-12 | [fruitfly_character_db_v1.1_2026-11-12.xlsx](fruitfly_character_db_v1.1_2026-11-12.xlsx) | 헤어 어레인지 벡터 추가: hair_styles(20) · hair_vector(60, 하루·시아·모아) · hair_sheets(21) / 3D 다각도 views_3d(270) 추가 / characters에 헤어·3D 집계 열 / 코드표에 헤어 ID / 안내 탭에 버전 기록 |
