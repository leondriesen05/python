import rewards

output = ""

for x in range(5):
    output += rewards.get_new_skin()
output_common_count = output.count('COMMON')
output_rare_count = output.count('RARE')
output_epic_count = output.count('EPIC')
output_legendary_count = output.count('LEGENDARY')
if 'COMMON' in output:
    print('%dx common' % output_common_count)
if 'RARE' in output:
    print('%dx rare' % output_rare_count)
if 'EPIC' in output:
    print('%dx epic' % output_epic_count)
if 'LEGENDARY' in output:
    print('%dx legendary' % output_legendary_count)
    