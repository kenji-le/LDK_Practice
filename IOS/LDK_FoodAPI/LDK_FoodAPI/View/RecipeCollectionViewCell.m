//
//  RecipeCollectionViewCell.m
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "RecipeCollectionViewCell.h"

@implementation RecipeCollectionViewCell

@synthesize currentRecipe, imgRecipe, lblTitle;

- (void)awakeFromNib {
    [super awakeFromNib];
    // Initialization code
}

- (void)setCellWithRecipe:(Recipe *)recipe {
    currentRecipe = recipe;
    [imgRecipe sd_setImageWithURL:[NSURL URLWithString:recipe.imageUrl] placeholderImage:[UIImage imageNamed:@"loading.png"]];
    
    [imgRecipe setFrame:CGRectMake(0, 0, self.bounds.size.width, self.bounds.size.height)];
    imgRecipe.contentMode = UIViewContentModeScaleAspectFit;
    
    [lblTitle setFrame:CGRectMake(MARGIN, self.bounds.size.height - MARGIN - lblTitle.bounds.size.height, self.bounds.size.width - MARGIN*2, lblTitle.frame.size.height)];
    lblTitle.text = recipe.title;
    [lblTitle sizeToFit];
    lblTitle.textColor = [UIColor whiteColor];
    NSLog(@"url = %@", recipe.imageUrl);
}

@end
