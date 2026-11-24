-- 11장: 실제 백엔드 서비스(Supabase 등 PostgreSQL)에서 쓰는 표와 권한 예시
-- 서비스마다 화면과 메뉴 이름이 다를 수 있습니다. AI에게 이 파일을 보여 주며 단계별로 물어보세요.

create table shows (
  id bigint generated always as identity primary key,
  movie text not null,
  starts_at timestamptz not null,
  seats int not null default 60
);

create table bookings (
  id bigint generated always as identity primary key,
  show_id bigint not null references shows(id),
  seat text not null,
  name text not null,
  phone4 char(4) not null check (phone4 ~ '^[0-9]{4}$'),
  created_at timestamptz default now(),
  unique (show_id, seat)            -- 같은 상영의 같은 좌석은 하나만: 동시 예매를 데이터베이스가 막는다
);

-- 손님에게 보여 줄 좌석 현황(이름·전화 없이)
create view seat_status as select show_id, seat from bookings;

create table orders (
  id bigint generated always as identity primary key,
  items jsonb not null,
  state text not null default '새 주문' check (state in ('새 주문', '준비 중', '받아 가세요', '완료')),
  created_at timestamptz default now()
);

create table scores (
  id bigint generated always as identity primary key,
  nick varchar(10) not null,
  score int not null check (score between 0 and 500),
  created_at timestamptz default now()
);

-- 권한(행 단위 보안): 누가 무엇을 읽고 쓰나
alter table shows enable row level security;
alter table bookings enable row level security;
alter table orders enable row level security;
alter table scores enable row level security;

create policy "상영은 누구나 읽기" on shows for select using (true);
create policy "예매는 누구나 새로 쓰기만" on bookings for insert with check (true);
create policy "예매 명단은 직원만 읽기" on bookings for select using (auth.role() = 'authenticated');
create policy "주문은 누구나 새로 쓰기" on orders for insert with check (state = '새 주문');
create policy "주문은 누구나 읽기" on orders for select using (true);
create policy "주문 상태는 직원만 바꾸기" on orders for update using (auth.role() = 'authenticated');
create policy "랭킹은 누구나 읽기" on scores for select using (true);
create policy "랭킹은 누구나 새로 쓰기만" on scores for insert with check (score between 0 and 500);
-- 지우기 정책은 만들지 않는다: 아무도 지울 수 없음
