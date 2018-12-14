[d1,d2,d3,d4,d5,d6] = textread('data.txt','%n%n%n%n%n%n');
raw = [d1,d2,d3,d4,d5,d6];
data = zeros(7,7,5,6);
count = 1;
d1 = 1:7;
d2 = 1:5;
for i1 = d1
  for i2 = d1
    for i3 = d2
      data(i1,i2,i3,:)=raw(count,:);
      count = count + 1;
    end
  end
end

figure
for i1 = 1:6
  for i2 = 1:5
   subplot(6,5,(i1-1)*5+i2);
   surf(d1,d1,data(:,:,i2,i1),'FaceColor',[.5,.5,.5]); 
  end
end