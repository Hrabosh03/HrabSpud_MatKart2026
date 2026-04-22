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

% calculate parameters and angle
% latitude
ua = atand(0.5); % ~26.5651 deg

%calculate latitude of the center points of the faces
gamma = atand( (2*sqrt(10*(5+sqrt(5)))) / sqrt(10*(25+11*sqrt(5))) );
ug = 90 - gamma; % ~ 52.6226

delta = acosd( (5 + 3*sqrt(5)) / (3*(3 + sqrt(5))) );
ud = 90 - gamma - delta; % ~ 10.8123 

% upper faces
% face 1
uk = ug; vk = 36;
u1b = 90; v1 = 36;
u2b = ua; v2 = 0;
u3b = ua; v3 = 72;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = 0; u2 = 90; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 1);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 2
uk = ug; vk = 108;
u1b = 90; v1 = 108;
u2b = ua; v2 = 72;
u3b = ua; v3 = 144;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = 0; u2 = 90; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 2);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 3
uk = ug; vk = 180;
u1b = 90; v1 = 180;
u2b = ua; v2 = 144;
u3b = ua; v3 = 216;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = 0; u2 = 90; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 3);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 4
uk = ug; vk = 252;
u1b = 90; v1 = 252;
u2b = ua; v2 = 216;
u3b = ua; v3 = 288;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = 0; u2 = 90; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 4);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 5
uk = ug; vk = 324;
u1b = 90; v1 = 324;
u2b = ua; v2 = 288;
u3b = ua; v3 = 360;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = 0; u2 = 90; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 5);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% middle upper faces
% face 6
uk = ud; vk = 36;
u1b = -ua; v1 = 36;
u2b = ua; v2 = 72;
u3b = ua; v3 = 0;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 6);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 7
uk = ud; vk = 108;
u1b = -ua; v1 = 108;
u2b = ua; v2 = 144;
u3b = ua; v3 = 72;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 7);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 8
uk = ud; vk = 180;
u1b = -ua; v1 = 180;
u2b = ua; v2 = 216;
u3b = ua; v3 = 144;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 8);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 9
uk = ud; vk = 252;
u1b = -ua; v1 = 252;
u2b = ua; v2 = 288;
u3b = ua; v3 = 216;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 9);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 10
uk = ud; vk = 324;
u1b = -ua; v1 = 324;
u2b = ua; v2 = 360;
u3b = ua; v3 = 288;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 10);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% middle lower faces
% face 11
uk = -ud; vk = 72;
u1b = ua; v1 = 72;
u2b = -ua; v2 = 36;
u3b = -ua; v3 = 108;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 11);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 12
uk = -ud; vk = 144;
u1b = ua; v1 = 144;
u2b = -ua; v2 = 108;
u3b = -ua; v3 = 180;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 12);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 13
uk = -ud; vk = 216;
u1b = ua; v1 = 216;
u2b = -ua; v2 = 180;
u3b = -ua; v3 = 252;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 13);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 14
uk = -ud; vk = 288;
u1b = ua; v1 = 288;
u2b = -ua; v2 = 252;
u3b = -ua; v3 = 324;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 14);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 15 (prekracujici nulty polednik)
uk = -ud; vk = 0;
u1b = ua; v1 = 0;
u2b = -ua; v2 = -36;
u3b = -ua; v3 = 36;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -40; u2 = 40; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 15);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% lower faces
% face 16
uk = -ug; vk = 72;
u1b = -90; v1 = 72;
u2b = -ua; v2 = 108;
u3b = -ua; v3 = 36;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -90; u2 = 0; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 16);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 17
uk = -ug; vk = 144;
u1b = -90; v1 = 144;
u2b = -ua; v2 = 180;
u3b = -ua; v3 = 108;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -90; u2 = 0; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 17);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 18
uk = -ug; vk = 216;
u1b = -90; v1 = 216;
u2b = -ua; v2 = 252;
u3b = -ua; v3 = 180;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -90; u2 = 0; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 18);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 19
uk = -ug; vk = 288;
u1b = -90; v1 = 288;
u2b = -ua; v2 = 324;
u3b = -ua; v3 = 252;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -90; u2 = 0; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 19);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% face 20 
uk = -ug; vk = 0;
u1b = -90; v1 = 0;
u2b = -ua; v2 = 36;
u3b = -ua; v3 = -36;
ub = [u1b, u2b, u3b]; vb = [v1, v2, v3];
u1 = -90; u2 = 0; v1 = floor((vk - 50)/10)*10; v2 = ceil((vk + 50)/10)*10;
subplot(4, 5, 20);
myGlobeFace(ub, vb, u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)
