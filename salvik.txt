const/32 v0,<Input A>
const/32 v1,<Input B>
const/32 v2,<Input C>
const/32 v3,1
sub-int v4,v3,v3
sub-int v5,v4,v3
move v6,v3
move v7,v4
sub-int v7,v7,v1
move v8,v0
move v9,v0
add-int v9,v0,v1
move v10,v4
move v11,v4
move v12,v3
:l0
add-int v11,v11,v1
add-int v10,v10,v0
move v13,v10
move v14,v4
move v15,v4
:l1
add-int v16,v13,v13
if-le v16,v1,:l2
sub-int v13,v13,v1
add-int v14,v14,v3
add-int v15,v15,v1
goto :l1
:l2
if-gt v13,v4,:l3
sub-int v13,v4,v13
:l3
move v17,v4
move v18,v3
:l4
add-int v17,v17,v13
add-int v18,v18,v3
if-le v18,v6,:l4
move v18,v3
:l5
sub-int v17,v17,v9
add-int v18,v18,v3
if-le v18,v12,:l5
if-ge v17,v4,:l6
move v5,v14
move v6,v12
move v7,v15
move v8,v10
move v9,v13
:l6
add-int v12,v12,v3
if-le v12,v2,:l0
return v6
