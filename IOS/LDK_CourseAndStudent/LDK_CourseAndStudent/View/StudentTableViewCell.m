//
//  StudentTableViewCell.m
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "StudentTableViewCell.h"

@implementation StudentTableViewCell

@synthesize lblName;
@synthesize delegate;

- (void)awakeFromNib {
    [super awakeFromNib];
    [self setSelectionStyle:UITableViewCellSelectionStyleNone];
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];
}

- (void)setCellWithStudent:(Student *)student atIndex:(NSIndexPath *)index {
    currentIndex = index;
    [lblName setText:student.studentName];
}

- (IBAction)deleteAction:(id)sender {
    if (delegate !=nil && [delegate respondsToSelector:@selector(studentTableViewCellDeleteAtIndex:)]) {
        [delegate studentTableViewCellDeleteAtIndex:currentIndex];
    }
}

- (IBAction)editAction:(id)sender {
    if (delegate != nil && [delegate respondsToSelector:@selector(studentTableViewCellEditAtIndex:)]) {
        [delegate studentTableViewCellEditAtIndex:currentIndex];
    }
}

@end
