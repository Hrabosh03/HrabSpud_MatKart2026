function[] = myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)
axis equal;
hold on;

% load outer points
[sb, db] = uv_to_sd(ub, vb, uk, vk);
[xb, yb] = fproj(R, sb, db);

% draw polygon vertices
plot(xb, yb, 'r.', 'MarkerSize', 5);
hold on

cx = mean(xb);
cy = mean(yb);
xb_clip = cx + (xb - cx) * 1.03; 
yb_clip = cy + (yb - cy) * 1.03;

% graticule
[XM, YM, XP, YP] = mygraticule(u1, u2, v1, v2, Du, Dv, du, dv, R, fproj,uk, vk);

% clip graticule
in_M = inpolygon(XM, YM, xb, yb);
XM(~in_M) = NaN;
YM(~in_M) = NaN;

in_P = inpolygon(XP, YP, xb_clip, yb_clip);
XP(~in_P) = NaN;
YP(~in_P) = NaN;

% draw graticule
plot(XM', YM', 'k');
hold on
plot(XP', YP', 'k');
axis equal

% Eurasia
eu = load('eurasie.txt');
u_eu = eu(:,1);
v_eu = eu(:,2);
[s_eu, d_eu] = uv_to_sd(u_eu, v_eu, uk, vk);
idx = find(s_eu<20);
s_eu(idx) = []; 
d_eu(idx) = [];
[x_eu, y_eu] = fproj(R, s_eu, d_eu);

% clip Eurasia
in_eu = inpolygon(x_eu, y_eu, xb_clip, yb_clip);
x_eu(~in_eu) = NaN; y_eu(~in_eu) = NaN;

plot(x_eu, y_eu, 'b', "linewidth", 0.5);


% North America
nam = load('s_amerika.txt');
u_nam = nam(:,1);
v_nam = nam(:,2);
[s_nam, d_nam] = uv_to_sd(u_nam, v_nam, uk, vk);
idx = find(s_nam<20);
s_nam(idx) = [];
d_nam(idx) = [];
[x_nam, y_nam] = fproj(R, s_nam, d_nam);

% clip North America
in_nam = inpolygon(x_nam, y_nam, xb_clip, yb_clip);
x_nam(~in_nam) = NaN; y_nam(~in_nam) = NaN;

plot(x_nam, y_nam, 'b', "linewidth", 0.5);


% South America
sam = load('j_amerika.txt');
u_sam = sam(:,1);
v_sam = sam(:,2);
[s_sam, d_sam] = uv_to_sd(u_sam, v_sam, uk, vk);
idx = find(s_sam<20);
s_sam(idx) = [];
d_sam(idx) = [];
[x_sam, y_sam] = fproj(R, s_sam, d_sam);

% clip South America
in_sam = inpolygon(x_sam, y_sam, xb_clip, yb_clip);
x_sam(~in_sam) = NaN; y_sam(~in_sam) = NaN;

plot(x_sam, y_sam, 'b', "linewidth", 0.5);


% Australia
au = load('australie.txt');
u_au = au(:,1);
v_au = au(:,2);
[s_au, d_au] = uv_to_sd(u_au, v_au, uk, vk);
idx = find(s_au<20);
s_au(idx) = [];
d_au(idx) = [];
[x_au, y_au] = fproj(R, s_au, d_au);

% clip Australia
in_au = inpolygon(x_au, y_au, xb_clip, yb_clip);
x_au(~in_au) = NaN; y_au(~in_au) = NaN;

plot(x_au, y_au, 'b', "linewidth", 0.5);


% Africa
af = load('afrika.txt');
u_af = af(:,1);
v_af = af(:,2);
[s_af, d_af] = uv_to_sd(u_af, v_af, uk, vk);
idx = find(s_af<20);
s_af(idx) = [];
d_af(idx) = [];
[x_af, y_af] = fproj(R, s_af, d_af);

% clip Africa
in_af = inpolygon(x_af, y_af, xb_clip, yb_clip);
x_af(~in_af) = NaN; y_af(~in_af) = NaN;

plot(x_af, y_af, 'b', "linewidth", 0.5);


% Antarctica
an = load('antarktida.txt');
u_an = an(:,1);
v_an = an(:,2);
[s_an, d_an] = uv_to_sd(u_an, v_an, uk, vk);
idx = find(s_an<20);
s_an(idx) = [];
d_an(idx) = [];
[x_an, y_an] = fproj(R, s_an, d_an);

% clip Antarctica
in_an = inpolygon(x_an, y_an, xb_clip, yb_clip);
x_an(~in_an) = NaN; y_an(~in_an) = NaN;

plot(x_an, y_an, 'b', "linewidth", 0.5);


% drawing limits
cmin = -2*R; 
cmax = -cmin;
xlim([cmin, cmax]);
ylim([cmin, cmax]);

axis off;
end