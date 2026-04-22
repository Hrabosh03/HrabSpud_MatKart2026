function [s, d] = uv_to_sd(u,v, uk, vk)

% original values u, v, uk, vk in degrees
% to radians
ur = u/180*pi;
vr = v/180*pi;
ukr = uk/180*pi;
vkr = vk/180*pi;

% calculate delta_v
d_v = vkr - vr;

% cartographic lattitude - s, to degrees
s = asin(sin(ur).*sin(ukr) + cos(ur).*cos(ukr).*cos(d_v))/pi*180;

% cartographic longitude
num = cos(ur).*sin(d_v);
denom = cos(ur).*sin(ukr).*cos(d_v)-sin(ur).*cos(ukr);

d = atan2(num,denom)/pi*180;
end