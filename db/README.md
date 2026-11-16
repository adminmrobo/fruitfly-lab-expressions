# 캐릭터 DB (엑셀) — 판별 보관

캐릭터 벡터(표정·동작·헤어·3D 등)가 바뀔 때마다 새 판을 **추가**합니다. 이전 판은 지우거나 덮어쓰지 않습니다.

- 파일 이름: `fruitfly_character_db_v{판}_{YYYY-MM-DD}.xlsx`
- 가장 최신 판: 아래 표의 맨 아래 줄
- 원본 원칙: 메타데이터·상태·사용 이력은 엑셀이 원본, 그림 파일과 변경 이력은 이 저장소가 원본 (시트 → 저장소 한 방향)

| 판 | 날짜 | 파일 | 바뀐 내용 |
|---|---|---|---|
| v1.0 | 2026-11-11 | [fruitfly_character_db_v1.0_2026-11-11.xlsx](fruitfly_character_db_v1.0_2026-11-11.xlsx) | 첫판: characters · expressions(216) · motion_sheets(59) · motion_segments(127) · usage · 코드표 |
| v1.1 | 2026-11-12 | [fruitfly_character_db_v1.1_2026-11-12.xlsx](fruitfly_character_db_v1.1_2026-11-12.xlsx) | 헤어 어레인지 벡터 추가: hair_styles(20) · hair_vector(60, 하루·시아·모아) · hair_sheets(21) / 3D 다각도 views_3d(270) 추가 / characters에 헤어·3D 집계 열 / 코드표에 헤어 ID / 안내 탭에 버전 기록 |
| v1.2 | 2026-11-12 | [fruitfly_character_db_v1.2_2026-11-12.xlsx](fruitfly_character_db_v1.2_2026-11-12.xlsx) | 헤어 그림 120장 반영 — hair_vector 60행의 image_status를 generated로 |
| v1.3 | 2026-11-14 | [fruitfly_character_db_v1.3_2026-11-14.xlsx](fruitfly_character_db_v1.3_2026-11-14.xlsx) | 공장(제조업 특화) 복장·동작 벡터 추가: factory_wear(8) · factory_poses(16) · factory_vector(144, 여섯 식구, planned) · factory_sheets(18) |
| v1.4 | 2026-11-14 | [fruitfly_character_db_v1.4_2026-11-14.xlsx](fruitfly_character_db_v1.4_2026-11-14.xlsx) | 공장 벡터 그림 144장 반영 — factory_vector 144행의 image_status를 generated로 |
| v1.5 | 2026-11-14 | [fruitfly_character_db_v1.5_2026-11-14.xlsx](fruitfly_character_db_v1.5_2026-11-14.xlsx) | 공장 벡터 144장 승인(approved) · 사용 이력: 배터리 AI 공장 시리즈 5개 페이지(①②③④·랩실)의 3D 공장 캐릭터 |
| v1.6 | 2026-11-15 | [fruitfly_character_db_v1.6_2026-11-15.xlsx](fruitfly_character_db_v1.6_2026-11-15.xlsx) | 확장 표정 E25 데헷(teehee) 추가 — expressions에 하루·시아·모아 3행(pending), 안내 탭 버전 기록 |
| v1.7 | 2026-11-15 | [fruitfly_character_db_v1.7_2026-11-15.xlsx](fruitfly_character_db_v1.7_2026-11-15.xlsx) | E25 데헷 그림 9장 반영 — 기본 3행 generated, 변형 shy·playful 6행 추가 |
| v1.8 | 2026-11-15 | [fruitfly_character_db_v1.8_2026-11-15.xlsx](fruitfly_character_db_v1.8_2026-11-15.xlsx) | E25 데헷 9장(하루·시아·모아 × 기본·shy·playful) 승인(approved) |
| v1.9 | 2026-11-16 | [fruitfly_character_db_v1.9_2026-11-16.xlsx](fruitfly_character_db_v1.9_2026-11-16.xlsx) | 시리즈 장면 그림 scene_art 추가 — 최적화 첫걸음 6장(표지 2·프롤로그 3·카드 썸네일 1, approved) · 사용 이력: optimization_3d_map first_step ①② 와 ahnboat.xyz 카드 |
