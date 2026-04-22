function[XM, YM, XP, YP] = mygraticule(u1, u2, v1, v2, Du, Dv, du, dv, R, fproj, uk, vk)

% parallels
XP = []; YP = [];
for u=u1:Du:u2
    vp = v1:dv:v2;
    up = ones(1,length(vp))*u;
    
    %neutral position
    [sp,dp] = uv_to_sd(up, vp, uk, vk);
    
    % rotation of a point at the equator
    idx = find(sp<0);
    sp(idx) = -sp(idx);

    % project parallels
    [xp,yp] = fproj(R,sp,dp);
    
    
    % add xp,yp to XP,YP
    XP = [XP; xp]; YP = [YP; yp];
end

% meridians
XM = []; YM = [];
for v=v1:Dv:v2
    um = u1:du:u2;
    vm = ones(1,length(um))* v;
    
    % neutral position
    [sm,dm] = uv_to_sd(um, vm, uk, vk);
    
    % rotation of a point at the equator
    idx = find(sm<0);
    sm(idx) = -sm(idx);

    % project meridian
    [xm,ym] = fproj(R,sm,dm);
    
    % new rows
    XM = [XM; xm]; YM = [YM; ym];
end


end


