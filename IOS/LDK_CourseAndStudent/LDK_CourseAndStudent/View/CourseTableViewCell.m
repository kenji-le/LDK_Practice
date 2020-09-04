//
//  CourseTableViewCell.m
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "CourseTableViewCell.h"

@implementation CourseTableViewCell

@synthesize lblName;
@synthesize delegate;

- (void)awakeFromNib {
    [super awakeFromNib];
    [self setSelectionStyle:UITableViewCellSelectionStyleNone];
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];
}

- (void)setCellWithCourse:(Course *)course atIndex:(NSIndexPath *)index {
    currentIndex = index;
    [lblName setText:course.courseName];
}

- (IBAction)deleteAction:(id)sender {
    if (delegate != nil && [delegate respondsToSelector:@selector(courseTableViewCellDeleteAtIndex:)]) {
        [delegate courseTableViewCellDeleteAtIndex:currentIndex];
    }
}

- (IBAction)editAction:(id)sender {
    if (delegate != nil && [delegate respondsToSelector:@selector(courseTableViewCellEditAtIndex:)]) {
        [delegate courseTableViewCellEditAtIndex:currentIndex];
    }
}

@end
