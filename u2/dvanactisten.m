clc
clear

% parameters
R = 6380*1000;
fproj = @gnom;
Du = 10;
Dv = 10;
du = 1;
dv = 1; 

axis equal

% compute parameters
alpha = 2 * asind( 2 / sqrt(10 - 2*sqrt(5)) );
ua = 90 - (180 - alpha); % u_alpha

gamma = atand( (2*sqrt(10*(5+sqrt(5)))) / sqrt(10*(25+11*sqrt(5))) );
ug = 90 - gamma; % u_gamma

delta = acosd( (5 + 3*sqrt(5)) / (3*(3 + sqrt(5))) );
ud = 90 - gamma - delta; % u_delta


% face 1 
uk = 90;
vk = 0;

% outer points, limits
u1b = ug; v1 = 36;
u2b = ug; v2 = 108;
u3b = ug; v3 = 180;
u4b = ug; v4 = 252;
u5b = ug; v5 = 324;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = 40; u2 = 90; v1 = -20; v2 = 380;

subplot(3, 4, 1);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 2 
uk = ua;
vk = 0;

u1b = ug; v1 = -36;
u2b = ug; v2 = 36;
u3b = ud; v3 = 36;
u4b = -ud; v4 = 0;
u5b = ud; v5 = -36;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -40; u2 = 80; v1 = -60; v2 = 60;

subplot(3, 4, 2);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 3
uk = ua;
vk = 72;

u1b = ug; v1 = 36;
u2b = ug; v2 = 108;
u3b = ud; v3 = 108;
u4b = -ud; v4 = 72;
u5b = ud; v5 = 36;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -40; u2 = 80; v1 = 10; v2 = 140;

subplot(3, 4, 3);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 4
uk = ua;
vk = 144;

u1b = ug; v1 = 108;
u2b = ug; v2 = 180;
u3b = ud; v3 = 180;
u4b = -ud; v4 = 144;
u5b = ud; v5 = 108;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -40; u2 = 80; v1 = 80; v2 = 210;

subplot(3, 4, 4);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 5
uk = ua;
vk = 216;

u1b = ug; v1 = 180;
u2b = ug; v2 = 252;
u3b = ud; v3 = 252;
u4b = -ud; v4 = 216;
u5b = ud; v5 = 180;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -40; u2 = 80; v1 = 150; v2 = 280;

subplot(3, 4, 5);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 6
uk = ua;
vk = 288;

u1b = ug; v1 = 252;
u2b = ug; v2 = 324;
u3b = ud; v3 = 324;
u4b = -ud; v4 = 288;
u5b = ud; v5 = 252;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -40; u2 = 80; v1 = 220; v2 = 350;

subplot(3, 4, 6);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 7
uk = -ua;
vk = 36;

u1b = ud; v1 = 36;
u2b = -ud; v2 = 72;
u3b = -ug; v3 = 72;
u4b = -ug; v4 = 0;
u5b = -ud; v5 = 0;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -80; u2 = 40; v1 = -30; v2 = 100;

subplot(3, 4, 7);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 8
uk = -ua;
vk = 108;

u1b = ud; v1 = 108;
u2b = -ud; v2 = 144;
u3b = -ug; v3 = 144;
u4b = -ug; v4 = 72;
u5b = -ud; v5 = 72;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -80; u2 = 40; v1 = 40; v2 = 170;

subplot(3, 4, 8);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 9
uk = -ua;
vk = 180;

u1b = ud; v1 = 180;
u2b = -ud; v2 = 216;
u3b = -ug; v3 = 216;
u4b = -ug; v4 = 144;
u5b = -ud; v5 = 144;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -80; u2 = 40; v1 = 110; v2 = 250;

subplot(3, 4, 9);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 10
uk = -ua;
vk = 252;

u1b = ud; v1 = 252;
u2b = -ud; v2 = 288;
u3b = -ug; v3 = 288;
u4b = -ug; v4 = 216;
u5b = -ud; v5 = 216;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -80; u2 = 40; v1 = 190; v2 = 320;

subplot(3, 4, 10);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 11
uk = -ua;
vk = 324;

u1b = ud; v1 = 324;
u2b = -ud; v2 = 360;
u3b = -ug; v3 = 360;
u4b = -ug; v4 = 288;
u5b = -ud; v5 = 288;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -80; u2 = 40; v1 = 260; v2 = 390;

subplot(3, 4, 11);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)


% face 12
uk = -90;
vk = 0;

u1b = -ug; v1 = 0;
u2b = -ug; v2 = 72;
u3b = -ug; v3 = 144;
u4b = -ug; v4 = 216;
u5b = -ug; v5 = 288;
ub = [u1b, u2b, u3b, u4b, u5b];
vb = [v1, v2, v3, v4, v5];
u1 = -90; u2 = -40; v1 = -20; v2 = 380;

subplot(3, 4, 12);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)
