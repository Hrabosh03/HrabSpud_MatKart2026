clc
clear

% symbolic variables
syms R u v

% gnomonic projection
x = R*tan(pi/2-u).*cos(v);
y = R*tan(pi/2-u).*sin(v);

% partial derivations
% simplify
fu = simplify(diff(x,u), 20);
fv = simplify(diff(x,v), 20);
gu = simplify(diff(y,u), 20);
gv = simplify(diff(y,v), 20);

% scale of meridian and parallels
mp2 = simplify(((fu^2 + gu^2)/R^2),20);
mr2 = simplify(((fv^2 + gv^2)/(R^2*(cos(u))^2)),20);
mp = simplify((sqrt(mp2)),20);
mr = simplify((sqrt(mr2)),20);

p = 2*(fu*fv + gu*gv); 

P1 = simplify((gu*fv - fu*gv)/(R^2*cos(u)), 'Steps',20);
P2 = simplify(mp * mr, 'Steps',50);

% maximal angular distortion
d_omega = 2*asin((abs(mr-mp))/(mr + mp));


% parameters of icosahedron
Rn = 6380;

% compute angle
ua = atand(0.5); % ~26.5651 st.

gamma = atand( (2*sqrt(10*(5+sqrt(5)))) / sqrt(10*(25+11*sqrt(5))) );
ug = 90 - gamma; % ~ 52.6226 deg

% point A (edge point)
un = ua; 
vn = 0;

% cartographic pole S1 
uk = ug; 
vk = 36;

% conversion relative to the coordinate system
[s, d] = uv_to_sd(un, vn, uk, vk);
s = s*pi/180;
d = d*pi/180;

xn = double(subs(x, {R, u, v}, {Rn, s, d}));
yn = -double(subs(y, {R, u, v}, {Rn, s, d}));

% partial derivations
fun = double(subs(fu, {R, u, v}, {Rn, s, d}));
fvn = double(subs(fv, {R, u, v}, {Rn, s, d}));
gun = double(subs(gu, {R, u, v}, {Rn, s, d}));
gvn = double(subs(gv, {R, u, v}, {Rn, s, d}));

% loc linear scales
mpn = double(subs(mp, {R, u, v}, {Rn, s, d}));
mrn = double(subs(mr, {R, u, v}, {Rn, s, d}));
pn = double(subs(p, {R, u, v}, {Rn, s, d}));

% area scale
Pn = double(subs(P1, {R, u, v}, {Rn, s, d}));
Pn1 = double(subs(P2, {R, u, v}, {Rn, s, d}));

% directive sigma_p
sigma_p = atan(gun/fun)-pi/2;
sigma_r = pi/2 - s;

% meridian convergence
c = abs(sigma_p);
c_deg = c*180/pi;

% maximal angular distortion
d_omegan = double(subs(d_omega, {R, u, v}, {Rn, s, d}))*180/pi;


% graticule
figure;
hold on
fproj = @gnom;
Du = 10; Dv = 10;
du = 1; dv = 1;

% interval
u1 = 0; u2 = 90;
v1 = -20; v2 = 90;

[XM, YM, XP, YP] = mygraticule(u1, u2, v1, v2, Du, Dv, du, dv, Rn, fproj, uk, vk);

% draw graticule
plot(XM', YM', 'k');
hold on
plot(XP', YP', 'k');
axis equal

% elliptical distortion
t = 0:pi/10:2*pi;
xe = mpn*cos(t)*1000;
ye = mrn*sin(t)*1000;
E = [xe; ye]; 

% rotation matrix
ROT = [cos(sigma_p), -sin(sigma_p); sin(sigma_p), cos(sigma_p)];

ER = ROT*E;
ER = ER';

% offset and drawing of an ellipse
plot(ER(:,1)+xn, ER(:,2)+yn, 'r', 'LineWidth', 1.5);

% visualization limits
xlim([-10000, 10000]);
ylim([-10000, 10000]);

