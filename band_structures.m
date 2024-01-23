mystartdefaults
BZpath
CohenBergstresser1966
recipunit = 1.e+10;
ekinscale = ((hbar*recipunit)^2/(2*elm))/qel; 
k_points = ans(1:3,:);
% Unit vectors in reciprocal space
g = zeros(4,3);
g(1:3,1) = cross(a(:,2),a(:,3))/cell_volume;
g(1:3,2) = cross(a(:,3),a(:,1))/cell_volume;
g(1:3,3) = cross(a(:,1),a(:,2))/cell_volume;

for i = 1:3
    g(4, i) = dot(g(1:3, i), g(1:3, i));
end
disp(g)
 % Build reciprocal lattice
min_norm = sqrt(min(g(4,:)));
limit = ceil(sqrt(sqrt(cutoff))/min_norm);
nodes = (2 * limit + 1)^3;
G_vectors = zeros(5,nodes);
n = 0;
% Loop to generate G vectors
% Equation 3.17
for h = -limit:limit
    for k = -limit:limit
        for l = -limit:limit
            n=n+1;
            G_vectors(1:3,n) = h * g(1:3,1) + k * g(1:3,2) + l * g(1:3,3);
            G_vectors(5,n) = dot(G_vectors(1:3,n),G_vectors(1:3,n));
            G_vectors(4,n) = sqrt(G_vectors(5,n));
        end
    end
end
disp(G_vectors)
G = sortrows(G_vectors', 4)';
% disp(G)
% Cutoff
num_G_vectors=1;
for n = 2:nodes
    if(G(5,n) <= cutoff)
        num_G_vectors=num_G_vectors + 1;
    end
end
% Loops for VG

H = zeros(num_G_vectors, num_G_vectors);
G_diff = zeros(5,1);
for n = 1:num_G_vectors
    VG(n) = 0;
    VS = 0;
    VA = 0;
    if G(5,n)==0
        VS = ff(m,1) * Rydberg;
        VA = 0;
    elseif G(5,n) == 3
        VS = ff(m,2) * Rydberg; 
        VA = ff(m,5) * Rydberg;
    elseif G(5,n) == 4
        VS = 0; 
        VA = ff(m,6) * Rydberg;
    elseif G(5,n) == 8
        VS = ff(m,3) * Rydberg; 
        VA = 0;
    elseif G(5,n) == 11
        VS = ff(m,4) * Rydberg; 
        VA = ff(m,7) * Rydberg;
    end
    % Equation 3.107
    VG(n) = VS * cos(2 * pi * dot(G(1:3,n),tau(1:3,1))) - 1i * VA * sin(2 * pi * dot(G(1:3,n),tau(1:3,1)));
end
% VG
% Hamiltonian
for j=1:num_G_vectors
    for i=1:num_G_vectors
        G_diff(1:3) = G(1:3,i) - G(1:3,j);
        G_diff(5) = dot(G_diff(1:3),G_diff(1:3));
        if(G_diff(5) <= Gs_max)
            for k=1:num_G_vectors
                if norm(G_diff(1:3)-G(1:3,k)) < tol
                    H(i,j) = VG(k);
                end
            end
        end
    end 
end
disp(H)
% Kinetic energy + plotting
spacing = ls(m);
ekinunit = ekinscale*(2*pi/spacing)^2;
num_k_points = 1:size(k_points,2);
for i = 1:size(k_points,2)
    for j = 1:num_G_vectors
        for k = 1:size(k_points,1)
            p(k)=k_points(k,i) - G(k,j);
        end
        % Equation [1] from Cohen and Bergstresser
        H(j,j) = ekinunit * (dot(p,p)) + VG(1);
    end
    [v,ev]=eig(H);
    E=real(diag(ev));
    [E,perm]=sort(E);
    v=v(:,perm);
    for g=1:nband
        bandstructure(g,i) = E(g);
    end
end

plot(num_k_points,bandstructure,'Color','blue','MarkerSize',2);
% disp(bandstructure)
% csvwrite('bandstructure_insb_fix.csv', bandstructure);
% fasdklfj
%find maximum/ridberg
third_band = max(bandstructure(3,:)) / Rydberg;
